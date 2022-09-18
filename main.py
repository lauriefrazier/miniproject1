#INF 601 - Advanced Programming with Python
#Laurie Frazier
#Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Creating Graphf for AAPL Stock
data = yf.download("AAPL", start="2022-09-02", end="2022-09-16")

aaplPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    aaplPrices.append(price)

print(aaplPrices)

#Create numpy array
aaplarray = np.array(aaplPrices)

#Create matplotlib graph, style, color, axis labels
plt.plot(aaplarray,'-o', color="gray")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Apple Closing Prices from 9/2 to 9/16")

#Show the graph
plt.savefig("Charts/aapl.png")
plt.show()


#Creating Chart for LMT Stock
data = yf.download("LMT", start="2022-09-02", end="2022-09-16")

lmtPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    lmtPrices.append(price)

print(lmtPrices)

#Create numpy array
lmtarray = np.array(lmtPrices)

#Create matplotlib graph, style, color, axis labels
plt.plot(lmtarray,'-o', color="blue")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Lockheed Martin Technologies Closing Prices from 9/2 to 9/16")

#Show the graph
plt.savefig("Charts/lmt.png")
plt.show()



#Creating Chart for CELH Stock
data = yf.download("CELH", start="2022-09-02", end="2022-09-16")

celhPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    celhPrices.append(price)

print(celhPrices)

#Create numpy array
celharray = np.array(celhPrices)

#Create matplotlib graph, style, color, axis labels
plt.plot(celharray,'-o', color="orange")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Celsius Closing Prices from 9/2 to 9/16")

#Show the graph
plt.savefig("Charts/celh.png")
plt.show()


#Creating Chart for BNED Stock
data = yf.download("BNED", start="2022-09-02", end="2022-09-16")

bnedPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    bnedPrices.append(price)

print(bnedPrices)

#Create numpy array
bnedarray = np.array(bnedPrices)

#Create matplotlib graph, style, color, axis labels
plt.plot(bnedarray,'-o', color="green")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Barnes and Noble Closing Prices from 9/2 to 9/16")

#Show the graph
plt.savefig("Charts/bned.png")
plt.show()


#Creating Chart for TSLA Stock
data = yf.download("TSLA", start="2022-09-02", end="2022-09-16")

tslaPrices = []

print(data["Adj Close"])

for price in data["Adj Close"]:
    tslaPrices.append(price)

print(tslaPrices)

#Create numpy array
tslaarray = np.array(tslaPrices)

#Create matplotlib graph, style, color, axis labels
plt.plot(tslaarray,'-o', color="red")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("Tesla Closing Prices from 9/2 to 9/16")

#Show the graph
plt.savefig("Charts/tsla.png")
plt.show()



