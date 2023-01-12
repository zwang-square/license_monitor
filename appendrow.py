# List that we want to add as a new row
import pandas as pd

rows = pd.read_csv('D:\ok.csv', header=None)
i = 0
for i in range(0, len(rows)):
    file_name = 'D:\ok\license{}.csv'.format(i)
    df = pd.read_csv(file_name, header=None)
    # Make data frame of above data
    data = rows[i:i + 1]
    df = pd.concat([df, data])
    # append dataframe to CSV file
    # df.columns = ['License Name', 'Total License Issued', 'Total License used', 'Timestamp']
    df.to_csv(file_name, header=None, mode='w', index=False)
    i += 1
