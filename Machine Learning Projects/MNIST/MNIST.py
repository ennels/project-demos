'''AICC 210 - Machine Learning - MNIST Classifier (KNN) - Elijah Walker'''
# Instructions were to build a classifier for MNIST that scores >97%
# accuracy on the test set. Hint: KNeighborsClassifier + grid search
# on weights and n_neighbors.

import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             ConfusionMatrixDisplay, classification_report)


# ============================================================
#                   PART 1 — PREVIEW DATA
# ============================================================

def load():
    '''Downloads MNIST from OpenML (cached after first run).'''
    print("\nLoading MNIST...")
    start = time.perf_counter()
    x, y = fetch_openml('mnist_784', as_frame=False, return_X_y=True)
    print(f'Loaded ({time.perf_counter() - start:.1f}s)')
    return x, y


def plot_digit(image_data):
    '''Plots one flattened 784-pixel row as a 28x28 image.'''
    plt.imshow(image_data.reshape(28, 28), cmap="binary")
    plt.axis("off")


def preview(x, y):
    '''Visual preview methods'''
    print("\nPreviewing...")

    # --- Quick previews ---
    print(f'\nShape:\t\t{x.shape}')
    print(f'Dtype:\t\t{x.dtype}')
    print(f'Pixel range:\t{x.min()} - {x.max()}')
    print(f'Labels:\t\t{np.unique(y)}')
    print(f'First 10:\t{y[:10]}\n')

    # --- Plotted visual ---
    plt.figure(figsize=(9, 9))
    for i in range(100):
        plt.subplot(10, 10, i + 1)
        plot_digit(x[i])
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


# ============================================================
#               PART 2 — CLEAN & PREPARE DATA
# ============================================================

def clean(x, y):
    '''Prepare the data for training'''
    print("\nAnalyzing data...\n")
    start = time.perf_counter()

    # --- Missing values ---
    # MNIST has none, but check anyway.
    print(f'Missing Values:\t\t{np.isnan(x).sum()}')

    # --- Fix label dtype ---
    # fetch_openml returns targets as strings ('5'), not ints.
    y = y.astype(np.uint8)
    print('Labels:\t\t\tconverted to uint8')

    # --- Drop useless columns ---
    # Some pixels are 0 for every image (image borders). Constant
    # columns add nothing to the distance calculation, so drop them.
    constant = np.where(x.min(axis=0) == x.max(axis=0))[0]
    x = np.delete(x, constant, axis=1)
    print(f'Useless Columns:\t{len(constant)} constant pixels dropped')

    # No scaling needed — every feature is already on the same 0-255
    # scale, so Euclidean distance is fair as-is.
    # No outliers/duplicates to hunt — every row is a valid image.

    elapsed = time.perf_counter() - start
    print(f'\nCleaning complete ({elapsed:.4f}s)\n'
          f'New shape: {x.shape[0]} rows, {x.shape[1]} columns\n')

    return x, y


def split(x, y):
    '''Splits the data into training and testing sets.'''

    # --- Split for Training/Testing ---
    # MNIST comes pre-split and pre-shuffled: first 60k train, last 10k
    # test. Using the standard split so accuracy is comparable to the
    # book's numbers.
    return x[:60000], x[60000:], y[:60000], y[60000:]


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def pick_params(x, y, n_sample=10000):
    '''Grid search over weights and n_neighbors (3-fold CV).'''
    # Full 60k with 5-fold would take ages. Search on a subsample,
    # then train the winner on everything.
    print(f'\n--- GRID SEARCH (3-fold CV, {n_sample} samples) ---')
    grid = {'weights': ['uniform', 'distance'],
            'n_neighbors': [3, 4, 5, 6]}
    search = GridSearchCV(KNeighborsClassifier(n_jobs=-1), grid, cv=3,
                          scoring='accuracy', verbose=1)
    start = time.perf_counter()
    search.fit(x[:n_sample], y[:n_sample])
    print(f'\nSearch complete ({time.perf_counter() - start:.1f}s)')

    res = search.cv_results_
    for params, mean, std in zip(res['params'], res['mean_test_score'],
                                 res['std_test_score']):
        print(f'{params}:\tacc = {mean:.4f} ± {std:.4f}')
    print(f'\nBest:\t{search.best_params_}')
    return search.best_params_


def train_knn(x_train, y_train, n_test, n_neighbors, weights):
    '''Selects and trains the model.'''

    # --- Select Model ---
    model = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights,
                                 n_jobs=-1)
    n = len(x_train) + n_test
    print(f'\n--- TRAINING ---\nModel:\t\t{model.__class__.__name__}'
          f' (k={n_neighbors}, weights={weights})\nSplit:\t\t'
          f'{len(x_train)/n:.0%} train / {n_test/n:.0%} test')

    # --- Train! ---
    # KNN "training" is just storing the data — the cost is at predict.
    start = time.perf_counter()
    model.fit(x_train, y_train)
    elapsed = time.perf_counter() - start
    print(f'\n\nTraining complete ({elapsed:.4f}s)')
    return model


# ============================================================
#                      PART 4 — RESULTS
# ============================================================

def results(model, x_test, y_test, x_test_raw):
    '''Prints results and plots the confusion matrix + misses.'''
    print("\n--- RESULTS ---")
    start = time.perf_counter()
    preds = model.predict(x_test)
    print(f'Predicted {len(x_test)} digits ({time.perf_counter() - start:.1f}s)')

    # --- Metrics ---
    acc = accuracy_score(y_test, preds)
    print(f'\nTest Accuracy:\t{acc:.4f}  ({"PASS" if acc > 0.97 else "FAIL"}'
          f' — target > 0.97)')
    print(f'Errors:\t\t{(preds != y_test).sum()} / {len(y_test)}')
    print(f'\n{classification_report(y_test, preds, digits=3)}')

    print(f'Predictions:\t{preds[:10]}')
    print(f'Actual:\t\t{y_test[:10]}\n')

    # --- Confusion matrix ---
    cm = confusion_matrix(y_test, preds)
    ConfusionMatrixDisplay(cm).plot(cmap='Blues')
    plt.title(f'KNN Confusion Matrix (acc = {acc:.4f})')
    plt.show()

    # --- Show some misclassified digits ---
    wrong = np.where(preds != y_test)[0][:25]
    plt.figure(figsize=(8, 8))
    for i, idx in enumerate(wrong):
        plt.subplot(5, 5, i + 1)
        plt.imshow(x_test_raw[idx].reshape(28, 28), cmap='binary')
        plt.title(f'{y_test[idx]} → {preds[idx]}', fontsize=9)
        plt.axis('off')
    plt.suptitle('Misclassified (true → predicted)')
    plt.tight_layout()
    plt.show()


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''This comment is here to satiate Pylint's ridiculous flagging system'''
    x, y = load()
    # preview(x, y)
    x_train, x_test, y_train, y_test = split(x, y)
    # Clean AFTER split so the dropped-pixel mask comes from train only.
    # (Constant-in-train pixels get dropped from test too, same indices.)
    keep = np.where(x_train.min(axis=0) != x_train.max(axis=0))[0]
    x_train, y_train = clean(x_train, y_train)
    x_test_raw = x_test  # keep full 784-pixel images for plotting
    x_test, y_test = x_test[:, keep], y_test.astype(np.uint8)

    # best = pick_params(x_train, y_train)  # Used this to choose the params
    best = {'n_neighbors': 4, 'weights': 'distance'}  # what the search found

    model = train_knn(x_train, y_train, len(x_test), **best)
    results(model, x_test, y_test, x_test_raw)


if __name__ == "__main__":
    main()