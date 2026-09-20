'''AICC 210 - Triple Threat Lab (mushrooms) - Elijah Walker'''
# Instructions were do regression on the Possum and Salary datasets,
# as well as classification on the Mushrooms set.

import time
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


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
    print(f'\nShape:\t{train.shape}\n')
    train.info()
    print(f'\n{train.head()}\n')

    print(f'Class balance:\n{train["class"].value_counts()}\n')
    print(f'Unique values per column:\n'
          f'{train.nunique().sort_values().to_string()}\n')


# ============================================================
#               PART 2 — CLEAN & PREPARE DATA
# ============================================================

def clean(train):
    '''Prepare the data for training'''
    print("\nAnalyzing data...\n")
    print(f'Shape:\t\t\t{train.shape[0]} rows, {train.shape[1]} columns')
    start = time.perf_counter()

    # No numeric columns, so cleaning just got a whole lot easier.

    # --- Duplicate rows ---
    if train.duplicated().sum() > 0:
        print(f'Duplicate Rows:\t\t{train.duplicated().sum()}')
        train = train.drop_duplicates()

    # --- Missing values ---  '?' is this dataset's NaN marker
    missing = (train == '?').sum()
    missing = missing[missing > 0]
    if not missing.empty:
        print(f'\nMissing Values ("?"):\t{missing.sum()}')
        for col in missing.index:
            print(f'\t"{col}" ({missing[col]} missing)')
        # Keep the rows; "unknown" becomes its own category
        train = train.replace('?', 'unknown')

    # --- Drop useless columns ---
    uniques = train.nunique()
    constant = uniques[uniques == 1].index.tolist()
    id_like = uniques[uniques == len(train)].index.tolist()
    drop = constant + id_like
    print(f'\nUseless Columns:\t{len(drop)}')
    for col in drop:
        print(f'\t"{col}" ({uniques[col]} unique values)')
    train = train.drop(columns=drop)

    # --- Encode ---  # 1 = 'p', or poisonous, 0 = 'e', or edible
    y = (train['class'] == 'p').astype(int)
    x = pd.get_dummies(train.drop(columns='class'), drop_first=True)

    elapsed = time.perf_counter() - start
    print(f'\nCleaning complete ({elapsed:.4f}s)\n'
          f'Encoded shape: {x.shape[0]} rows, {x.shape[1]} features\n')
    return x, y


def split(x, y):
    '''Splits the data into training and testing sets.'''
    # stratify keeps the e/p ratio identical in train and test
    return train_test_split(x, y, test_size=0.2, stratify=y)


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def train_model(x_train, y_train, model, n_test):
    '''Trains the given classifier.'''
    n = len(x_train) + n_test
    print(f'\n--- TRAINING ---\nModel:\t\t{model.__class__.__name__}'
          f'\nSplit:\t\t{len(x_train)/n:.0%} train / {n_test/n:.0%} test')

    start = time.perf_counter()
    model.fit(x_train, y_train)
    elapsed = time.perf_counter() - start
    print(f'\nTraining complete ({elapsed:.4f}s)')
    return model


# ============================================================
#                      PART 4 — RESULTS
# ============================================================

def results(model, x_train, y_train, x_test, y_test):
    '''Prints classification metrics and plots the confusion matrix.'''
    print("\n--- RESULTS ---")
    preds = model.predict(x_test)

    # --- Metrics ---
    print(f'Train Acc:\t{model.score(x_train, y_train):.4f}')
    print(f'Test Acc:\t{accuracy_score(y_test, preds):.4f}')

    # --- Confusion matrix ---
    cm = confusion_matrix(y_test, preds)
    print(f'\nConfusion Matrix (rows=actual, cols=predicted):\n{cm}')
    # Bottom-left cell = poisonous predicted edible = the dangerous mistake
    print(f'\nPoisonous called edible:\t{cm[1, 0]}\n')


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''This comment is here to satiate Pylint's ridiculous flagging system'''
    train = load('mushrooms.csv')
    # preview(train)
    x, y = clean(train)
    x_train, x_test, y_train, y_test = split(x, y)

    # --- Decision Tree ---
    # model = DecisionTreeClassifier(max_depth=5)
    # model = train_model(x_train, y_train, model, len(x_test))
    # results(model, x_train, y_train, x_test, y_test)

    # --- Logistic Regression ---
    model = LogisticRegression(max_iter=1000)
    model = train_model(x_train, y_train, model, len(x_test))
    results(model, x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
