'''AICC 210 - Machine Learning - Linear Regression Lab - Elijah Walker'''
# Assignment was to perform linear regression on a linear regression dataset.
# Top level stuff :)

import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
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
    print(train.shape)
    train.info()
    print(train.describe())
    print(train.head())

    # --- Plotted visual ---
    plt.scatter(train[['x']], train['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# Visualizing the data shows zero outliers.
# But that's not always conclusive...


# ============================================================
#               PART 2 — CLEAN & PREPARE DATA
# ============================================================

def clean(train):
    '''Prepare the data for training'''

    # --- Show missing values ---
    if train.isnull().values.any():
        print(f'Missing Values:\n{train[train.isnull().any(axis=1)]}')

    # The y column had one missing value, very likely a misinput.
    # I adjusted the dataset manually to fix this.

    # --- Detect outliers ---
    q1 = train.quantile(0.25)
    q3 = train.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = train[((train < lower) | (train > upper)).any(axis=1)]
    if not outliers.empty:
        print(f'Outliers:\n{outliers}')

    # --- Ignore outliers ---
    train = train[((train >= lower) & (train <= upper)).all(axis=1)]

    # This method originally detected one outlier, the x value in
    # the same row that was missing a y value.

    return train


def split(train):
    '''Splits the data into training and testing sets.'''

    # --- Split for Training/Testing ---
    x, y = train[['x']], train['y']

    return train_test_split(x, y, test_size=0.2)
    # I got rid of 'random_state' to make the results feel more real.


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def train_model(x_train, y_train, n_test):
    '''Selects and trains the model.'''

    # --- Select Model ---
    model = LinearRegression()
    n = len(x_train) + n_test
    print(f'\n--- TRAINING ---\nModel:\t\t{model}')
    print(f'Split:\t\t{len(x_train)/n:.0%} train / {n_test/n:.0%} test')

    # --- Train! ---
    start = time.perf_counter()
    model.fit(x_train, y_train)
    elapsed = time.perf_counter() - start
    print(f'\nTraining complete ({elapsed:.4f}s)')
    return model


# ============================================================
#                      PART 4 — RESULTS
# ============================================================

def results(model, x_train, y_train, x_test, y_test):
    '''Prints results and plots the fitted line.'''
    print("\n\n--- RESULTS ---")
    preds = model.predict(x_test)

    # --- Metrics ---
    print(f'Train R2:\t{model.score(x_train, y_train):.3f}')
    print(f'Test R2:\t{model.score(x_test, y_test):.3f}')
    print(f'Test MAE:\t{mean_absolute_error(y_test, preds):.3f}')
    print(f'Test RMSE:\t{root_mean_squared_error(y_test, preds):,.3f}')

    print(f'\nEquation:\ty = {model.coef_[0]:.4f}x {"-" if model.intercept_ < 0 else "+"} {abs(model.intercept_):.4f}')

    print(f'\nPredictions:\t{preds[:5]}')
    print(f'Actual:\t\t{y_test[:5].values}\n')

    # --- Plot ---
    plt.figure(figsize=(8, 6))
    plt.scatter(x_test, y_test, alpha=0.6, label='Actual (test)')
    plt.plot(x_test, preds, color='red', linewidth=2, label='Fitted line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{model.__class__.__name__}  (y = {model.coef_[0]:.3f}x + {model.intercept_:.3f})')
    plt.legend()
    plt.show()


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''Main. Nuff said.'''
    train = load('linear regression dataset.csv')
    # preview(train)
    train = clean(train)
    x_train, x_test, y_train, y_test = split(train)
    model = train_model(x_train, y_train, len(x_test))
    results(model, x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
