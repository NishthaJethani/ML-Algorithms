import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv('tvmarketing.csv')
x=dataframe['TV']
y=dataframe['Sales']


def linear_regression(x, y):
    mean_x=x.mean()
    mean_y=y.mean()
    B1_numerator=((x-mean_x)*(y-mean_y)).sum()
    B1_denominator=((x-mean_x)**2).sum()
    B1=B1_numerator/B1_denominator

    B0=mean_y-(B1*mean_x)

    print("y=",B1,"x+",B0)
    return B1, B0

def plot_graph():
    B1, B0=linear_regression(x, y)
    plt.scatter(dataframe['TV'], dataframe['Sales'])
    plt.plot(x, B1*x+B0)
    plt.show()

plot_graph()

def predict(x_predict):
    B1, B0=linear_regression(x, y)    
    y_predicted=B0+(B1*x_predict)
    return y_predicted

y_predicted=predict(1783)
print(y_predicted)
