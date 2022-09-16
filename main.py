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

#Create matplotlib graph, style, color, axis labels
plt.plot(aaplarray,'-o', color="teal")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Apple Closing Prices from 8/30 to 9/14")

#Show the graph
plt.savefig("Charts/aapl.png")
plt.show()



