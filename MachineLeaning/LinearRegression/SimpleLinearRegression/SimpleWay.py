"""
y = b0 + b1*x

x is independent variable
y is dependent variable

b1,b0 is constant
b1 = slop
Without going into the mathematical details, we present the result here:

 b1 = SS_xy/SS_xx

 b0 = y' - b1*x'

where SS_xy is the sum of cross-deviations of y and x:
 SS_xy = sum((x - x')(y-y'))

and SS_xx is the sum of squared deviations of x:
 SS_xx = sum((x-x')**2)

Note: The complete derivation for finding least squares estimates in simple linear regression can be found here.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def estimate_coefficient(x, y):
    m_x = np.mean(x)  # calculate the mean of the x
    m_y = np.mean(y)  # calculate  the mean of the y

    SS_xy = np.sum((x - m_x) * (y - m_y))
    SS_xx = np.sum((x - m_x) ** 2)
    b1 = SS_xy / SS_xx
    b0 = m_y - b1 * m_x
    return (b0, b1)


def plot_regression_line(x, y, b):
    plt.scatter(x=x, y=y, color='m', marker="*")  # Original points
    Y_predict = b[0] + b[1]*x
    plt.plot(x,Y_predict,color = 'r')

    # putting labels
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')

    # function to show plot
    plt.show()


if __name__ == "__main__":
    data = pd.read_csv("../../../DataSets/Company.csv")
    experence = data['YearsExperience']
    salary = data['Salary']

    # estimating coefficients
    b = estimate_coefficient(experence, salary)

    # plotting regression line
    plot_regression_line(experence, salary, b)
