# project-demos

Python labs from my AI & Cloud Computing AAS at the College of Western Idaho. Most of it comes from AICC 210 (Machine Learning). There's also a data mining project from AICC 170 and assignments from AICC 120 (Python for Data Analysis). Each folder has its own code, data, and plots, so every lab runs by itself.

```
pip install -r requirements.txt
```

## Machine Learning (AICC 210)

### [SVM: Wisconsin Breast Cancer](machine-learning/SVM)
Predicts whether a tumor is malignant or benign. It uses the two features most correlated with the diagnosis, worst concave points and worst perimeter. I trained a linear SVM and an RBF SVM on a stratified 80/20 split and plotted both decision boundaries. Linear got 95.6% accuracy and RBF got 96.5%, with 0.95 recall on malignant cases.

### [MNIST: KNN Classifier](machine-learning/MNIST)
KNN on the full 70k MNIST set. I dropped the border pixels that never change, grid-searched k and the weighting with 3-fold CV, then tested on the standard 10k split. The best setup was k=4 with distance weighting, at just over 97%. The same folder has a second lab, `ClassifyPerformance.py`, which covers logistic regression with stratified 5-fold CV, precision/recall curves, and a dummy classifier as a baseline.

### [Regression & Classification ("Triple Threat")](machine-learning/Regression%20%26%20Classification)
Three datasets in one lab. For salary vs. experience and the possum body measurements, I used polynomial regression and picked the degree with cross-validation. For the mushroom dataset (edible or poisonous), I compared logistic regression against a decision tree. It includes correlation heatmaps, fit curves, and the tree plot.

### [Rakhi Sales](machine-learning/Rakhi%20Sales)
I cleaned the Delhi Rakhi sales data, checked correlations, and fit a polynomial regression that predicts sales from customer visits. The plot shows the fitted equation, and R², RMSE, and MAE print to the terminal.

### [Ice Cream Sales](machine-learning/Ice%20Cream%20Sales)
I rewrote a polynomial regression tutorial as a single reusable function. Then I fit sales vs. temperature at degrees 1, 2, 10, and 20 to show what underfitting and overfitting look like.

### [Basic Linear Regression](machine-learning/Basic%20Linear%20Regression)
My first regression lab: preview the data, check for outliers with IQR, handle missing values, fit, and evaluate.

### [Spotify Stats](machine-learning/Spotify%20Stats)
Preprocessing practice on Spotify track data. It covers finding missing values, ordinal/boolean/one-hot encoding, choosing features, splitting, and scaling.

## Data Mining (AICC 170)

### [Weather Station Analysis](data-mining/weather-station-analysis)
Seven questions about weather station data. Each one gets its own SQL query (GROUP BY, HAVING, aggregates) and a seaborn chart: box, violin, regression, or grouped bar. I wrote it against MariaDB, but it also runs on SQLite with no setup.

## Python for Data Analysis (AICC 120)

- [A11: Cleaning Data](data-analysis/Project%20Submissions/A11_CleaningData). Replaces the zeros in a 10×10 matrix with each row's non-zero mean. It also has the extra-credit "shortened" version, which turned out to be the only one in the class that worked.
- [A10: Baseball Manager](data-analysis/Project%20Submissions/A10_UserInteractivity). A menu-driven CLI for adding, editing, and deleting players and their batting averages. It uses a Player class and saves to CSV.
- [A09: Files & Exceptions](data-analysis/Project%20Submissions/A09_FilesAndExceptions). Reads and writes user records as text and JSON, with exception handling.
- [A08: Classes](data-analysis/Project%20Submissions/A08_Classes). Employee and Manager classes that use inheritance, plus test scripts.
- [Misc Scripts](data-analysis/Misc%20Scripts). Basics like lists, dicts, and conditionals. Also a quiz appeal I wrote as runnable Python, which got me full credit.

I add new labs every semester. The latest is the SVM lab from Fall 2026.
