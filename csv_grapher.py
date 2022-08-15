import csv
import matplotlib.pyplot as plt
import pandas as pandasForSortingCSV

file = 'stock_list.csv'
# print(file)
# csvData = pandasForSortingCSV.read_csv(file)
# file = csvData.sort_values(["peRatio"], 
#                     axis=0,
#                     ascending=[True], 
#                     inplace=True)

# print(file)
# plt.rcParams['font.size'] = '10'

# xs = []
# ys = []
# symbols = []

with open(file, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        #if len(row[2]) != 0 and len(row[4]) != 0 and len(row[1]) != 0:
        plt.plot(row[2], row[4], 'bo', markersize='3')
        plt.annotate(row[2], (row[2], row[4]), textcoords="offset points", xytext = (0,3), ha = "center")

#print(len(xs), len(ys), len(symbols))



#for k in range(len(xs)):
    # xs[k] = float(xs[k])
    # ys[k] = float(ys[k])
    
plt.xlabel('PE')
plt.ylabel('PB')


plt.grid()
plt.show()  
