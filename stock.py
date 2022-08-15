import yfinance as yf
import matplotlib.pyplot as plt
import time
import csv

class stock_analysis:
    def __init__(self, stock_name):
        self.stock_name = stock_name
    
    

    def info(self):
        tmp_stock = yf.Ticker(self.stock_name)
        tmp = tmp_stock.info

        try:
            stock = {'symbol' : tmp['symbol'],
            'sector' : tmp['sector'],
            'currentPrice': tmp['currentPrice'], 
            'trailingPE' : tmp['trailingPE'], 
            'revenueGrowth' : tmp['revenueGrowth']}

            data = ['currentPrice', 'trailingPE', 'revenueGrowth']
            for x in range(len(data)):
                stock[data[x]] = float(stock[data[x]])
            
            plt.plot(stock['trailingPE'],stock['revenueGrowth'],'bo', markersize='3')
            plt.annotate(stock['symbol'], (stock['trailingPE'],stock['revenueGrowth']), textcoords="offset points", xytext = (0,3), ha = "center")

            print(stock)
        except:
            return None



stock_list = []
with open('screener (1).csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        stock_list.append(row[0])


for x in stock_list:
    startTime = time.time()
    r = stock_analysis(x)
    r.info()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

plt.show()