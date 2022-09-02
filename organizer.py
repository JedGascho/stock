import pandas as pandasForSortingCSV
import pandas as pd

class organize:
    def main(file_name, sorter):
        #takes file name inputer from grapher.py
        file = file_name
        
        csvData = pandasForSortingCSV.read_csv(file)

        #sorts data lowest to highest along X AXIS
        file = csvData.sort_values([sorter], 
                            axis=0,
                            ascending=[True], 
                            inplace=True)

        #saves new data to stock_list.csv
        df = pd.DataFrame(csvData)
        df.to_csv('stock_list.csv', encoding='utf-8')

        return [df.columns[1], df.columns[3]]
