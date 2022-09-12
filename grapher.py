import csv
import matplotlib.pyplot as plt
import os
#import from organizer.py
from organizer import organize

import statistics 

#import headers
xvar = 'Current ROI (TTM)'
yvar = '% Price Change (1 Week)'
symbol = 'Ticker'
sector = 'Sector'




file = [f for f in os.listdir('.') if f.endswith('.csv')]
file = str(file[0])

column = organize.main(file, xvar)

plt.rcParams['figure.figsize'] = 30, 10

x_avg = []
y_avg = []

with open(file, 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        try:
            x_avg.append(float(row[xvar]))
            y_avg.append(float(row[yvar]))
            plt.plot(float(row[xvar]), float(row[yvar]), 'bo', markersize='3')
            #annotates
            plt.annotate(row[symbol], (float(row[xvar]), float(row[yvar])), textcoords="offset points", xytext = (0,3), ha = "center")
        except ValueError:
            pass


plt.axhline(y = (sum(y_avg)/len(y_avg)), color='r')
plt.axvline(x = (sum(x_avg)/len(x_avg)), color='r')

plt.axhline(y = (statistics.median(y_avg)), color='y')
plt.axvline(x = (statistics.median(x_avg)), color='y')


plt.xlabel(xvar)
plt.ylabel(yvar)

outliers = []
for x in range(len(x_avg)):
    if float(row[xvar]):
        pass

plt.title(xvar + ', ' + yvar, fontsize = 20)
plt.grid()

tmp = os.listdir('./figs')
if len(tmp) == 0:
  fig_name = './figs/fig.png'
else:
  fig_name = './figs/fig ' + '(' + str(len(tmp)) + ').png'
plt.savefig(fig_name)

os.remove('stock_list.csv')
#plt.show()
