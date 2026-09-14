'''AICC 210 - Machine Learning - SVM Boundary Lab - Elijah Walker'''
# Instructions were to preview and scale data, train and plot a
# linear-kernel SVM boundary, and compare redo with RBF kernel.

import time
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.inspection import DecisionBoundaryDisplay


# ============================================================
#                   PART 1 — PREVIEW DATA
# ============================================================

# Preview methods I've used in the past with this same ML template
# don't work on this dataset- it's got all sorts of data arrangements
# compiled into one dictionary.

def preview(file, train):
    '''Visual preview methods'''
    # print("\nPreviewing...")
    # for label, data in file.items():
    #     print(f'{label}:\n{data}\n\n')

    # print("\nCorrelation with Target:")
    # print(train.corr()['target'].abs().sort_values(ascending=False).head(10))

    # "Worst Concave Points" and "Worst Perimeter" have the highest
    # correlations with the Target data, so we can plot 'em.

    # --- Plotted visual ---
    x1, x2 = 'worst concave points', 'worst perimeter'
    # plt.figure(figsize=(8, 6))
    # for t, name in enumerate(file.target_names):
    #     subset = train[train['target'] == t]
    #     plt.scatter(subset[x1], subset[x2], alpha=0.5, label=name)
    # plt.xlabel(x1)
    # plt.ylabel(x2)
    # plt.title('Wisconsin Breast Cancer — raw data')
    # plt.legend()
    # plt.savefig('svm_corrplot.jpg')
    # plt.show()

    # And if you do plot 'em, you can see there's a pretty clear area
    # and angle where a boundary belongs.

    return [x1, x2]


# ============================================================
#               PART 2 — CLEAN & PREPARE DATA
# ============================================================

# Looks like the only crucial file items to me are 'data', 'target', and
# 'feature_names' for column labels. Everything else is just descriptive.

# That said, with the crucial nature of the data, and considering the
# reliability of its source, my gut response is to leave it be.

def clean(train, features):
    '''For this dataset, just removes unneeded columns.'''
    train = train[features + ['target']].copy()

    return train


def split(train, features):
    '''Splits the data into training and testing sets, then scales data.'''

    # --- Split for Training/Testing ---
    x, y = train[features], train['target']
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, stratify=y
    )

    # --- Scale ---
    # To do this right, we have to fit scaler to the training set,
    # then scale the test set by the same number.

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    pd.DataFrame(x_train, columns=features)
    # fit_transform returns numpy array, use above line to get columns back
    x_test = scaler.transform(x_test)

    return x_train, x_test, y_train, y_test


# ============================================================
#                PART 3 — SELECT MODEL & TRAIN
# ============================================================

def train_svm(x_train, x_test, y_train, kernel):
    '''Selects and trains the model.'''

    # --- Select Model ---
    model = SVC(kernel=kernel, C=1.0)
    n = len(x_train) + len(x_test)
    print(f'Split:\t\t{len(x_train)/n:.0%} train / {len(x_test)/n:.0%} test')

    # --- Train! ---
    start = time.perf_counter()
    model.fit(x_train, y_train)
    elapsed = time.perf_counter() - start
    print(f'Training complete ({elapsed:.4f}s)\n')

    return model


# ============================================================
#                      PART 4 — RESULTS
# ============================================================


def results(model, x_train, y_train, x_test, y_test, features, target_names):
    '''Prints classification metrics and plots the decision boundary.'''
    preds = model.predict(x_test)

    # --- Metrics ---
    print(f'Train Acc:\t{model.score(x_train, y_train):.3f}')
    print(f'Test Acc:\t{accuracy_score(y_test, preds):.3f}')

    # SVMs have metric options other models don't, obviously. Check it out:
    print(f'Support Vecs:\t{len(model.support_)} of {len(x_train)}')
    print(f'\nConfusion Matrix (rows=actual, cols=predicted):\n'
          f'{confusion_matrix(y_test, preds)}')
    print(f'\n{classification_report(y_test, preds,
          target_names=target_names)}')

    # --- Equation --- (linear only)
    if model.kernel == 'linear':
        (w1, w2), b = model.coef_[0], model.intercept_[0]
        print(f'Boundary equation:\t{w1:.4f}*x1 + {w2:.4f}*x2 + {b:.4f} = 0\n\n\n')

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(8, 6))
    DecisionBoundaryDisplay.from_estimator(
        model, x_train, response_method='predict', alpha=0.3, ax=ax
    )

    # Below is a script to graph actual support vectors alongside data points.
    for t, name in enumerate(target_names):
        mask = y_test == t
        ax.scatter(x_test[mask, 0], x_test[mask, 1], alpha=0.7, label=name)
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
               s=80, facecolors='none', edgecolors='k',
               label='Support vectors')

    # And this is script that marks the model's errors:
    wrong = preds != y_test
    ax.scatter(x_test[wrong, 0], x_test[wrong, 1], marker='x', c='red', s=60,
               label='Misclassified')

    ax.set_xlabel(f'{features[0]} (scaled)')
    ax.set_ylabel(f'{features[1]} (scaled)')
    ax.set_title(f'SVM Boundary — {model.kernel} kernel  '
                 f'(test acc {accuracy_score(y_test, preds):.3f})')
    ax.legend()
    plt.show()


# ============================================================
#                      MAIN FUNCTION
# ============================================================

def main():
    '''Main.'''
    file = sklearn.datasets.load_breast_cancer()
    train = pd.DataFrame(file.data, columns=file.feature_names)
    train['target'] = file.target

    features = preview(file, train)
    # print("File parameters mapped for training:\n"
    #       f"{train}")

    x_train, x_test, y_train, y_test = split(train, features)
    train = clean(train, features)
    print("--- RESULTS ---\n\n")
    for kernel in ('linear', 'rbf'):
        print(f"--- {kernel.upper()} ---\n")
        model = train_svm(x_train, x_test, y_train, kernel)
        results(model, x_train, y_train, x_test, y_test, features, file.target_names)


if __name__ == "__main__":
    main()
