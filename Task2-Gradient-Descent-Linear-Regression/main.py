import matplotlib.pyplot as plt
import numpy as np
import csv
import random

x = []
y = []
with open('dataset.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        x.append(int(i['x']))
        y.append(float(i['y']))
m=len(y)
def hypothesis(x, theta0, theta1):
    return theta0*theta1*x

def cost(theta0, theta1,x,y):
    sum = 0
    for i in range(m):
        sum += (hypothesis(x[i], theta0, theta1) - y[i])**2
    return sum/2*m

def gradientDescent(theta0, theta1, alpha):
    sum_theta0 = 0
    for i in range(m):
        sum_theta0 += (hypothesis(x[i], theta0, theta1) - y[i])

    sum_theta1 = 0
    for i in range(0, m):
        sum_theta1 += (hypothesis(x[i], theta0, theta1) - y[i])*x[i]

    theta0 = theta0 - alpha * sum_theta0/m
    theta1 = theta1 - alpha * sum_theta1/m
    return theta0, theta1

if __name__ == "__main__":
    theta0 = random.random()
    theta1 = random.random()
    alpha = 0.001

    for i in range(100):   
        theta0, theta1 = gradientDescent(theta0, theta1, alpha)
    print("theta0 \t\t theta1")
    print(theta0,theta1)
    
    # plotting:
    plt.plot(x, y , 'x')
    result=[]
    for i in x:
        result.append(hypothesis(i, theta0, theta1))
    plt.plot(x, result ,color = "red")
    plt.show()
