'''AICC 210 - Machine Learning - Triple Threat Lab (salary) - Elijah Walker'''
# Instructions were do regression on the Possum and Salary datasets,
# as well as classification on the Mushrooms set.

import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from sklearn.pipeline import make_pipeline


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
    print(f'\n{train.head()}\n')

    # --- Plotted visual ---
    plt.scatter(train[['YearsExperience']], train['Salary'])
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

    num = train.select_dtypes("number").drop(columns=["case"],
                                             errors="ignore")
    target = "Salary"
    print(num.corr()[target].drop(target).abs().sort_values(ascending=False))
    sns.heatmap(num.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.tight_layout()
    plt.savefig("salary_corr.png")

    # Draws a heatmap of correlations between the numeric columns.
    # Pretty unnecessary for this dataset, there being two numeric columns.


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
        train = train.dropna()

    # --- Drop useless columns ---
    uniques = train.nunique()
    constant = uniques[uniques == 1].index.tolist()
    # Cols with only one unique value
    # id_like = uniques[uniques == len(train)].index.tolist()
    # Cols with unique values for every row. We actually
    # want to keep those here.
    drop = constant
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

    # No binary columns to encode.

    # --- Column dtype check ---
    for col in train.select_dtypes(exclude='number').columns:
        converted = pd.to_numeric(
            train[col].str.replace(r'[,$%]', '', regex=True),
            errors='coerce')
        if converted.notna().mean() > 0.9:
            train[col] = converted
            print(f'{col}: converted to numeric')

    # --- Detect outliers ---
    print("\nDetecting Outliers...")
    for col in train.select_dtypes('number').columns:
        q1 = train[col].quantile(0.25)
        q3 = train[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outies = (train[col] < lower) | (train[col] > upper)
        if outies.sum() > 0:
            print(f'\t"{col}" ({outies.sum()} outliers)')
        train = train[~outies]

    train = train.copy()

    # No "impossible" values in these datasets

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
    x, y = train[['YearsExperience']], train['Salary']

    return train_test_split(x, y, test_size=0.2)
    # I removed the random_state parameter for fun.


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def pick_degree(x, y, max_degree=5):
    '''Cross-validated R2 for each degree.'''
    print('\n--- DEGREE SEARCH (5-fold CV) ---')
    for d in range(1, max_degree + 1):
        pipe = make_pipeline(PolynomialFeatures(d, include_bias=False),
                             LinearRegression())
        scores = cross_val_score(pipe, x, y, cv=5, scoring='r2')
        print(f'Degree {d}:\tR2 = {scores.mean():.3f} ± {scores.std():.3f}')


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

    # --- Equation ---  coef_[i] is x^(i+1)
    terms = [f'{c:+.4f}x^{i+1}' if i else f'{c:+.4f}x'
             for i, c in enumerate(model.coef_)]
    eq = f'y = {model.intercept_:.4f} ' + ' '.join(terms)
    print(f'\nEquation:\t{eq}')

    print(f'\nPredictions:\t{preds[:5]}')
    print(f'Actual:\t\t{y_test.iloc[:5].values}\n')

    # --- Plot ---
    x_sorted = x_test.sort_values('YearsExperience')
    plt.figure(figsize=(8, 6))
    plt.scatter(x_test, y_test, alpha=0.4, label='Actual (test)')
    plt.plot(x_sorted, model.predict(poly.transform(x_sorted)), color='red',
             linewidth=2, label='Fitted curve')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.title(f'Polynomial Regression D{poly.degree}  ({eq})')
    plt.legend()
    plt.show()


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''This comment is here to satiate Pylint's ridiculous flagging system'''
    train = load('Salary_dataset.csv')
    # preview(train)
    train = clean(train)
    x_train, x_test, y_train, y_test = split(train)
    # pick_degree(x_train, y_train)  # Helps me decide the degree
    model, poly = train_poly(x_train, y_train, 1, len(x_test))
    results(model, poly, x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
