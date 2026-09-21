# project-demos

Python coursework from the Artificial Intelligence & Cloud Computing AAS at the College of Western Idaho — AICC 210 (Machine Learning) and AICC 120 (Python for Data Analysis). Each folder is a self-contained lab with source, data, and output plots.

Setup: `pip install -r requirements.txt`

## Machine learning (AICC 210)

| Lab | What it does | Techniques | Results / output |
|---|---|---|---|
| [SVM — Wisconsin Breast Cancer](machine-learning/SVM) | Classifies tumors as malignant or benign using the two features most correlated with the target (worst concave points, worst perimeter). Trains linear and RBF-kernel SVMs and plots each decision boundary. | SVC, StandardScaler, stratified 80/20 split, confusion matrix, classification report | 95.6% linear / 96.5% RBF accuracy, 0.95 recall on malignant; boundary plots |
| [MNIST — KNN classifier](machine-learning/MNIST) | Handwritten-digit classification on the full 70k MNIST set. Drops constant border pixels, grid-searches k and weighting with 3-fold CV, evaluates on the standard 10k test split. Includes a second lab (`ClassifyPerformance.py`) on logistic regression with stratified 5-fold CV, precision/recall curves, and a dummy-classifier baseline. | KNeighborsClassifier, GridSearchCV, LogisticRegression, StratifiedKFold | >97% test accuracy (k=4, distance weighting); confusion matrix, misclassified samples |
| [Regression & Classification — "Triple Threat" lab](machine-learning/Regression%20%26%20Classification) | Three datasets in one lab: salary vs. experience and possum morphometrics (polynomial regression with cross-validated degree selection and correlation heatmaps), mushrooms (edible/poisonous classification, logistic regression vs. decision tree). | PolynomialFeatures pipelines, cross_val_score, LogisticRegression, DecisionTreeClassifier, seaborn | R² / RMSE per model; fit curves, correlation heatmaps, decision tree |
| [Rakhi Sales](machine-learning/Rakhi%20Sales) | Polynomial regression predicting sales count from customer visits on Delhi Rakhi sales data, after cleaning and correlation analysis. | Polynomial regression, train/test R², RMSE, MAE | fit curve with equation, terminal metrics |
| [Ice Cream Sales](machine-learning/Ice%20Cream%20Sales) | Refactors a polynomial-regression tutorial into one reusable function, then fits sales vs. temperature at degrees 1, 2, 10, and 20 to show under- and overfitting. | PolynomialFeatures + LinearRegression | fit curves per degree |
| [Basic Linear Regression](machine-learning/Basic%20Linear%20Regression) | First regression lab — preview, IQR outlier check, missing-value handling, fit, and evaluate. | LinearRegression, train/test R², RMSE, MAE | plot, terminal output |
| [Spotify Stats](machine-learning/Spotify%20Stats) | Preprocessing lab on Spotify track data: missing-value audit, ordinal / boolean / one-hot encoding, feature selection, train/test split, scaling. | pandas, get_dummies, StandardScaler | processed feature matrix |

## Data mining (AICC 170)

| Lab | What it does | Techniques | Output |
|---|---|---|---|
| [Weather Station Analysis](data-mining/weather-station-analysis) | Seven analytical questions answered with hand-written SQL against MariaDB, visualized with seaborn — box, violin, regression, and grouped bar charts. Runs on SQLite with no setup. | SQL (GROUP BY, HAVING, aggregates), SQLAlchemy, seaborn | seven annotated charts |

## Python for data analysis (AICC 120)

| Assignment | What it does | Concepts |
|---|---|---|
| [A11 — Cleaning Data](data-analysis/Project%20Submissions/A11_CleaningData) | Replaces zeros in a 10×10 matrix with each row's non-zero mean. Includes the extra-credit "shortened" version — the only working submission in the class. | List comprehensions, statistics, data cleaning |
| [A10 — Baseball Manager](data-analysis/Project%20Submissions/A10_UserInteractivity) | Menu-driven CLI to add, edit, and delete players with batting average, persisted to CSV through a Player class. | File I/O, classes, input validation, CSV |
| [A09 — Files & Exceptions](data-analysis/Project%20Submissions/A09_FilesAndExceptions) | Read and write user records in text and JSON with exception handling. | File I/O, JSON, try/except |
| [A08 — Classes](data-analysis/Project%20Submissions/A08_Classes) | Employee and Manager classes with inheritance and test scripts. | OOP, inheritance |
| [Misc scripts](data-analysis/Misc%20Scripts) | Fundamentals — lists, dicts, conditionals — plus a quiz appeal written as runnable code (full credit awarded). | Python basics |

## Status

Ongoing — new labs added each semester. Latest: SVM (Fall 2026).
