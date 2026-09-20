'''AICC 210 - Machine Learning - Fixing "Ice Cream" Lab - Elijah Walker'''
# Instructions were to simplify the script to one function that can do all
# kinds of polynomial regression and visualize the results.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def getdata(file):
    '''Load the CSV and return x, y.'''
    data = pd.read_csv(file)
    data.head()

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    return X, y


def plotdata(X, y):
    '''Visualize the data.'''
    plt.scatter(X, y, color="red")
    plt.xlabel("Temperature in Celsius")
    plt.ylabel("Ice Cream Sales")
    plt.title("Ice Cream Sales Data")
    plt.show()


# All-in-one function to create polynomial regression model and visualize it
def polyregression(X, y, degree):
    '''Fit a polynomial regression model of varioius degrees and visualize.'''
    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(x_poly, y)

    plt.scatter(X, y, color="red")
    plt.plot(X, model.predict(x_poly), color="blue")
    plt.xlabel("Temperature in Celsius")
    plt.ylabel("Ice Cream Sales")
    plt.title(f"Polynomial Regression D{degree}")
    plt.show()


def main():
    '''Main function'''
    X, y = getdata('Ice_cream selling data.csv')
    plotdata(X, y)
    for degree in (1, 2, 10, 20):  # Could also hook this up to user input...
        polyregression(X, y, degree)


if __name__ == "__main__":
    main()
