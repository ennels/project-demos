'''AICC 210 - Machine Learning - Rakhi Sales Lab - Elijah Walker'''
# Instructions were to clean the data and perform polynomial regression.
# You will soon learn that I am a formatting freak...

import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, mean_absolute_error


# ============================================================
#                   PART 1 — PREVIEW DATA
# ============================================================

def load(file):
    '''Loads the CSV file into a Pandas DataFrame.'''
    try:
        return pd.read_csv(file)
    except FileNotFoundError as exc:
        raise SystemExit(f"Error: '{file}' not found.") from exc


def preview(train):
    '''Visual preview methods'''
    print("\nPreviewing...")

    # --- Quick previews ---
    print(f'\nShape:\t{train.shape}\n')
    train.info()
    print(f'\n{train.describe()}')
    print(f'\n{train.head()}')

    # --- Plotted visual ---
    plt.scatter(train[['No_Of_Customers_Visit']], train['Sales_Count'])
    plt.xlabel('No_Of_Customers_Visit')
    plt.ylabel('Sales_Count')
    plt.show()

# The relationship between customers and sales is the only one
# that carries a strong enough correlation to be worth modeling.


# ============================================================
#               PART 2 — CLEAN & PREPARE DATA
# ============================================================

def clean(train):
    '''Prepare the data for training'''
    print("\nAnalyzing data...\n")
    print(f'Shape:\t\t\t{train.shape[0]} rows, {train.shape[1]} columns')
    start = time.perf_counter()

    # Ignore duplicate rows
    if train.duplicated().sum() > 0:
        print(f'Duplicate Rows:\t\t{train.duplicated().sum()}')
        train = train.drop_duplicates()

    # --- Show missing values ---
    if train.isnull().values.any():
        print(f'\nMissing Values:\t\t{train.isnull().sum().sum()}')
        # --- Missing values ---
        missing = train.isnull().sum()
        missing = missing[missing > 0]
        for col in missing.index:
            print(f'\t"{col}" ({missing[col]} missing)')
        train.loc[:, 'Delhi_Zone'] = train['Delhi_Zone'].fillna('Unknown')
        train.loc[:, 'Average_Temperature_C'] = train['Average_Temperature_C'].fillna(train['Average_Temperature_C'].median())

    # --- Drop useless columns ---
    uniques = train.nunique()
    constant = uniques[uniques == 1].index.tolist()
    # Cols with only one unique value
    id_like = uniques[uniques == len(train)].index.tolist()
    # Cols with unique values for every row
    labels = ['Shop_Name']  # Manual. Shop Name is just a label
    drop = constant + id_like + labels
    print(f'\nUseless Columns:\t{len(drop)}')
    for col in drop:
        print(f'\t"{col}" ({uniques[col]} unique values)')
    train = train.drop(columns=drop)

    # --- Fix text columns ---
    for col in train.select_dtypes(exclude='number').columns:
        train[col] = (train[col]
                      .str.replace(r'[^\w\s&()]', '', regex=True)
                      # get rid of weird characters
                      .str.strip()
                      .str.title())  # correct weird capitalization

    # --- Encode binary columns ---
    train['Weekend_Sale'] = train['Weekend_Sale'].map({'Yes': 1, 'No': 0})

    # --- Column dtype check ---
    for col in train.select_dtypes(exclude='number').columns:
        converted = pd.to_numeric(
            train[col].str.replace(r'[,$%]', '', regex=True),
            errors='coerce')
        if converted.notna().mean() > 0.9:
            train[col] = converted
            print(f'{col}: converted to numeric')
    # This doesn't change anything in THIS dataset, but its purpose is
    # to convert text columns to numeric if they should be.

    # --- Detect outliers ---
    print("\nDetecting Outliers...")
    for col in train.select_dtypes('number').columns:
        q1 = train[col].quantile(0.25)
        q3 = train[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 3 * iqr
        upper = q3 + 3 * iqr
        # 3x IQR is pretty generous, but this dataset has some crazy outliers.

        outies = (train[col] < lower) | (train[col] > upper)
        if outies.sum() > 0:
            print(f'\t"{col}" ({outies.sum()} outliers)')
        train = train[~outies]

    train = train.copy()

    # --- Impossible values ---
    impossible = (
        (train['Sales_Count'] < 0) |
        (train['No_Of_Customers_Visit'] < 0) |
        (train['Price'] <= 0) |
        (train['Sales_Count'] > train['No_Of_Customers_Visit']) |
        (train['Average_Temperature_C'] > 48)
    )
    print(f'\nImpossible values found in {impossible.sum()} rows.')
    train = train[~impossible].copy()

    # --- Quality checks ---
    # print(f'\nClean shape:\t{train.shape}')
    # print(f'Missing left:\t{train.isnull().sum().sum()}')
    # print(train.describe().round(2).to_string())

    elapsed = time.perf_counter() - start
    print(f'\nCleaning complete ({elapsed:.4f}s)\n'
          f'New shape: {train.shape[0]} rows, {train.shape[1]} columns\n')

    return train


def split(train):
    '''Splits the data into training and testing sets.'''

    # --- Split for Training/Testing ---
    x, y = train[['No_Of_Customers_Visit']], train['Sales_Count']

    return train_test_split(x, y, test_size=0.2)
    # I removed the random_state parameter for fun.


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def train_poly(x_train, y_train, degree, n_test):
    '''Selects and trains the model.'''

    # --- Select Model ---
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    x_train_poly = poly.fit_transform(x_train)
    model = LinearRegression()
    n = len(x_train) + n_test
    print(f'\n--- TRAINING ---\nModel:\t\t{model.__class__.__name__}'
          f' (degree {degree})\nSplit:\t\t{len(x_train)/n:.0%} '
          f'train / {n_test/n:.0%} test')

    # --- Train! ---
    start = time.perf_counter()
    model.fit(x_train_poly, y_train)
    elapsed = time.perf_counter() - start
    print(f'\n\nTraining complete ({elapsed:.4f}s)')
    return model, poly


# ============================================================
#                      PART 4 — RESULTS
# ============================================================

def results(model, poly, x_train, y_train, x_test, y_test):
    '''Prints results and plots the fitted curve.'''
    print("\n--- RESULTS ---")
    x_train_poly = poly.transform(x_train)
    x_test_poly = poly.transform(x_test)
    preds = model.predict(x_test_poly)

    # --- Metrics ---
    print(f'Train R2:\t{model.score(x_train_poly, y_train):.3f}')
    print(f'Test R2:\t{model.score(x_test_poly, y_test):.3f}')
    print(f'Test MAE:\t{mean_absolute_error(y_test, preds):.3f}')
    print(f'Test RMSE:\t{root_mean_squared_error(y_test, preds):.3f}')

    # --- Equation ---  coef_[0] is x, coef_[1] is x^2
    b0, (b1, b2) = model.intercept_, model.coef_
    eq = f'y = {b0:.4f} + {b1:.4f}x {"-" if b2 < 0 else "+"} {abs(b2):.4f}x^2'
    print(f'\nEquation:\t{eq}')

    print(f'\nPredictions:\t{preds[:5]}')
    print(f'Actual:\t\t{y_test.iloc[:5].values}\n')

    # --- Plot ---
    x_sorted = x_test.sort_values('No_Of_Customers_Visit')
    plt.figure(figsize=(8, 6))
    plt.scatter(x_test, y_test, alpha=0.4, label='Actual (test)')
    plt.plot(x_sorted, model.predict(poly.transform(x_sorted)), color='red', linewidth=2, label='Fitted curve')
    plt.xlabel('No_Of_Customers_Visit')
    plt.ylabel('Sales_Count')
    plt.title(f'Polynomial Regression D{poly.degree}  ({eq})')
    plt.legend()
    plt.show()


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''Main. Nuff said.'''
    train = load('rakhi_sales_delhi.csv')
    # preview(train)
    train = clean(train)
    x_train, x_test, y_train, y_test = split(train)
    model, poly = train_poly(x_train, y_train, 2, len(x_test))
    results(model, poly, x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
