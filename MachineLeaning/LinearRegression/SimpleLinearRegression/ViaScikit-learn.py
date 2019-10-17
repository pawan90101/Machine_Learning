import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def estimate_coefficient(real_x, real_y):
    #trainning data always between 70-80% remaining is tesing data
    training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)
    #test size set to 30% then all other is training data 70% .
    lin = LinearRegression()
    lin.fit(training_x,training_y)
    plot_regression_line(training_x, training_y,testing_x,testing_y, lin)

def plot_regression_line(training_x,training_y,testing_x,testing_y,lin):
    pred_y = lin.predict(training_x)
    plt.scatter(x=training_x,y=training_y,color = 'm',marker='*') #for training
    #plt.scatter(x=testing_x,y=lin.predict(testing_x),color = 'm',marker='*') #for testing
    """
    verify equation
    b1 = coefficient
    bo = intercept
    
    pred_yTest = lin.predict(testing_x)
    b1 = lin.coef_
    b0 = lin.intercept_

    predectY_value = b0 + b1*1.5 #take any value of x actual y = 37731
    print(predectY_value)
    """


    plt.plot(training_x,pred_y,color = "r")
    plt.xlabel("Expirence")
    plt.ylabel('salary')
    plt.title('Salary and Expirence')
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv("../../../DataSets/Company.csv")
    #expirence = data['YearsExperience']
    #salary = data['Salary']
    expirence = data.iloc[:,0].values
    salary = data.iloc[:,1].values
    expirence = expirence.reshape(-1,1)
    salary = salary.reshape(-1, 1)

    # estimating coefficients
    b = estimate_coefficient(expirence, salary)