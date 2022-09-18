# miniproject1
## INF 601 - Advanced Programming in Python
### Laurie Frazier

'pip install -r requirements.txt'

### This project is intended to print a graph of the closing prices of Apple, Lockheed Martin, Celsius, Barnes and Noble and Telsa.

#### Code Design
After importing the required packages, the yfinance package will allow a download of the chosen stocks information and will translate into a table.
Selecting the Adj Close data, it will print off the Closing Price from that day.
The data will then append to be used for a NumPy array

#### Creating the Graph
Creating the graph, using matplotlib's ploting package, creating the graph from the array.
The styling choices I made were each graph used the same dots given by the -o input.
1. Apple is represented as <span style= "color:gray"> gray</span>
2. Lockheed Martin is detailed as <span style= "color:blue"> blue</span>
3. Celsius is colored <span style= "color:orange"> orange</span>
4. Barnes and Noble data is <span style= "color:green"> green</span>
5. Telsa is <span style= "color:red"> red</span>