#INF 601 - Advanced Programming with Python
#Laurie Frazier
#Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


data = yf.download("AAPL", start="2022-08-30", end="2022-09-14")

aaplPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    aaplPrices.append(price)

print(aaplPrices)

#Create numpy array
aaplarray = np.array(aaplPrices)

#Create matplotlib graph
plt.plot(aaplarray)

#Show the graph
plt.savefig("Charts/aapl.png")
plt.show()


