'''AICC 210 - Machine Learning - Classifying Performance Lab - Elijah Walker'''
# I believe this is the script you want me to reformat around a main() function...
# I also trimmed the tutorial-style commentary, focusing purely on functionality.

import os
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
)
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score,
    train_test_split,
)

matplotlib.use("Agg")

RANDOM_STATE = 42
FIG_DIR = "figures"
TARGET_NAMES = ["malignant", "benign"]


def section(title):
    '''Print a section header.'''
    line = "=" * 70
    print(f"\n{line}\n{title}\n{line}")


def save_fig(fig, name):
    '''Save a figure to FIG_DIR and close it.'''
    path = f"{FIG_DIR}/{name}"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved chart -> {path}")


def print_metrics(y_true, y_pred):
    '''Print accuracy, precision, recall, and F1.'''
    print(f"  Accuracy:  {accuracy_score(y_true, y_pred):.4f}")
    print(f"  Precision: {precision_score(y_true, y_pred, zero_division=0):.4f}")
    print(f"  Recall:    {recall_score(y_true, y_pred, zero_division=0):.4f}")
    print(f"  F1:        {f1_score(y_true, y_pred, zero_division=0):.4f}")


def load_data():
    '''Load the breast cancer dataset and return (x, y).'''
    section("DATA: Breast Cancer Wisconsin")
    x, y = load_breast_cancer(return_X_y=True)
    print(f"Samples: {x.shape[0]}, Features: {x.shape[1]}")
    print(f"Class balance -> malignant: {(y == 0).sum()}, benign: {(y == 1).sum()}")
    return x, y


def run_cross_validation(model, x, y):
    '''Stratified 5-fold cross-validation with a bar chart of fold accuracy.'''
    section("CROSS-VALIDATION (Stratified 5-Fold)")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    cv_scores = cross_val_score(model, x, y, cv=cv, scoring="accuracy")

    for i, score in enumerate(cv_scores, start=1):
        print(f"  Fold {i}: accuracy = {score:.4f}")
    print(f"  Mean accuracy: {cv_scores.mean():.4f}  (+/- {cv_scores.std():.4f})")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar([f"Fold {i}" for i in range(1, len(cv_scores) + 1)], cv_scores, color="#4C72B0")
    ax.axhline(cv_scores.mean(), color="#C44E52", linestyle="--",
               label=f"Mean = {cv_scores.mean():.3f}")
    ax.set_ylim(0.8, 1.0)
    ax.set_ylabel("Accuracy")
    ax.set_title("5-Fold Stratified Cross-Validation Accuracy")
    ax.legend()
    save_fig(fig, "cv_scores.png")


def run_confusion_matrix(model, x, y):
    '''Fit on a held-out split, print and plot the confusion matrix.'''
    section("CONFUSION MATRIX")
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE
    )
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print("  TN, FP, FN, TP:", *cm.ravel())

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=TARGET_NAMES)
    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    ax.set_title("Confusion Matrix — Breast Cancer Test Set")
    save_fig(fig, "confusion_matrix.png")

    return y_test, y_pred


def run_precision_recall_f1(y_test, y_pred):
    '''Print precision/recall/F1 and the full classification report.'''
    section("PRECISION, RECALL, F1")
    print_metrics(y_test, y_pred)
    print()
    print(classification_report(y_test, y_pred, target_names=TARGET_NAMES))


def run_imbalanced_example():
    '''Compare a dummy classifier vs. logistic regression on 95/5 imbalanced data.'''
    section("IMBALANCED DATA (95% / 5%)")
    x_imb, y_imb = make_classification(
        n_samples=5000,
        n_features=15,
        n_informative=5,
        weights=[0.95, 0.05],
        flip_y=0.01,
        random_state=RANDOM_STATE,
    )
    xi_train, xi_test, yi_train, yi_test = train_test_split(
        x_imb, y_imb, test_size=0.3, stratify=y_imb, random_state=RANDOM_STATE
    )
    print(f"Test set class balance -> legit: {(yi_test == 0).sum()}, fraud: {(yi_test == 1).sum()}")

    dummy = DummyClassifier(strategy="most_frequent", random_state=RANDOM_STATE)
    dummy.fit(xi_train, yi_train)
    print("\n-- Dummy (most_frequent) --")
    print_metrics(yi_test, dummy.predict(xi_test))

    imb_model = LogisticRegression(max_iter=5000, random_state=RANDOM_STATE)
    imb_model.fit(xi_train, yi_train)
    print("\n-- Logistic Regression --")
    print_metrics(yi_test, imb_model.predict(xi_test))

    return imb_model, xi_test, yi_test


def run_threshold_tradeoff(imb_model, xi_test, yi_test):
    '''Plot precision/recall vs. threshold and the PR curve.'''
    section("PRECISION / RECALL vs. THRESHOLD")
    y_scores = imb_model.predict_proba(xi_test)[:, 1]
    precisions, recalls, thresholds = precision_recall_curve(yi_test, y_scores)

    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.plot(thresholds, precisions[:-1], label="Precision", color="#4C72B0")
    ax.plot(thresholds, recalls[:-1], label="Recall", color="#DD8452")
    ax.set_xlabel("Decision Threshold")
    ax.set_ylabel("Score")
    ax.set_title("Precision & Recall vs. Decision Threshold")
    ax.legend()
    ax.grid(alpha=0.3)
    save_fig(fig, "precision_recall_tradeoff.png")

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(recalls, precisions, color="#55A868")
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.set_title("Precision-Recall Curve")
    ax.grid(alpha=0.3)
    save_fig(fig, "pr_curve.png")


def main():
    '''Run all lab sections.'''
    os.makedirs(FIG_DIR, exist_ok=True)

    x, y = load_data()
    model = LogisticRegression(max_iter=5000, random_state=RANDOM_STATE)

    run_cross_validation(model, x, y)
    y_test, y_pred = run_confusion_matrix(model, x, y)
    run_precision_recall_f1(y_test, y_pred)

    imb_model, xi_test, yi_test = run_imbalanced_example()
    run_threshold_tradeoff(imb_model, xi_test, yi_test)

    section("DONE")
    print(f"All figures saved in ./{FIG_DIR}/")


if __name__ == "__main__":
    main()
