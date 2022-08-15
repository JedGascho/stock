import csv
import matplotlib.pyplot as plt

#import from organizer.py
from organizer import organize

#input UNORGANIZED csv file, in the format ("symbol", "peRatio", "stockPrice", "pbRatio")
organize.main('screener.csv')

#organized file
file = 'stock_list.csv'

with open(file, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        #plots point where x axis is peRatio, and y axis is pbRatio
        try:
            plt.plot(float(row[2]), float(row[4]), 'bo', markersize='3')

            #annotates
            plt.annotate(row[1], (float(row[2]), float(row[4])), textcoords="offset points", xytext = (0,3), ha = "center")
        except ValueError:
            pass

plt.xlabel('PE')
plt.ylabel('PB')

plt.grid()
plt.show()  
