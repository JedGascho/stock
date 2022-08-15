#USED FOR TESTING PURPOSES ONLY

import csv
import pandas as pandasForSortingCSV
import pandas as pd
import numpy as np
file = 'screener (2).csv'

csvData = pandasForSortingCSV.read_csv(file)
print(csvData)
file = csvData.sort_values(["peRatio"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)

df = pd.DataFrame(csvData)

df.to_csv('stock_list.csv', encoding='utf-8')
# col_count = df.shape[0]
# print(col_count)

# with open('stock_list.csv', 'w') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     for x in range(len(col_count)):
#         # write the data
#         writer.writerow(csvData[x])

# with open('stock_list.csv', 'r') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)