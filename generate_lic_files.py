import pandas as pd
from datetime import datetime
from csv import writer
import posixpath
import os


# delete all the blank lines in files
def delblankline(infile, outfile):
    infopen = open(infile, 'r')
    outfopen = open(outfile, 'w')
    k = infopen.readlines()
    for line in k:
        if line.split():
            # replace each row from ‘:'&';' to ','
            rs = line.strip(')')
            newname = rs.strip('')
            newname = newname.replace(':', ',')
            newname = newname.replace(';', ',')
            outfopen.writelines(newname)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()


# format the file
def format_file():
    with open('D;\lic', "r") as f:
        ll = f.readlines()
    with open('D:\lic', "w") as f:
        for line in ll:
            str1 = line[0:9]
            if str1 == 'Users of ':
                f.write(line)


format_file()

delblankline('D:\lic', 'D:\ok.csv')

# add timestamp to a new column to file
time = datetime.now()
str_current_date = time.strftime("%Y-%m-%d %H:%M:%S")
df = pd.read_csv('D:\ok.csv', header=None)
# names=['License Name', 'Total license issued', 'Total license used', 'time']
for i in range(0, len(df)):
    df.iloc[i][0] = df.iloc[i][0][9:]
    # get number from the string column 2
    num_1 = 0
    txt_1 = df.iloc[i][1]
    for num_1 in txt_1.split():
        if num_1.isdigit():
            df.iloc[i][1] = num_1
    # get number from the string column 3
    num_2 = 0
    txt_2 = df.iloc[i][2]
    for num_2 in txt_2.split():
        if num_2.isdigit():
            df.iloc[i][2] = num_2
    i += 1
df[3] = str_current_date
df.to_csv('D:\ok.csv', header=None, index=False)

# start to generate each file for each row
lines = pd.read_csv('D:\ok.csv', header=None)
i = 0
for row in lines.values:
    file_name = lines[i:i+1][0]
    a_path = 'D:\license_list'
    a_file = file_name.to_string(index=False)
    file_path = os.path.join(a_path, a_file)
    file_tile = file_path + ".csv".format(i)
    row.tofile(file_tile, sep=",", format="%s")
    i += 1


# Append new row to exit license files seperately each hour
rows = pd.read_csv('/app/projects/asic_sandbox/zwang/sandbox/lic_list/ok.csv', header=None)
i = 0
for i in range(0, len(rows)):
    file_name = rows[i:i + 1][0]
    a_path = '/app/projects/asic_sandbox/zwang/sandbox/lic_list/license_list/'
    a_file = file_name.to_string()
    file_tile = '/app/projects/asic_sandbox/zwang/sandbox/lic_list/license_list/' + a_file + '.csv'.format(i)
    # file_path = '/app/projects/asic_sandbox/zwang/sandbox/lic_list/ok/{}.csv'.format(i)
    df = pd.read_csv(file_tile, header=None)
    # Make data frame of above data
    data = rows[i:i + 1]
    df = pd.concat([df, data])
    # append dataframe to CSV file
    df.to_csv(file_tile, mode='w', header=False, index=False)
    i += 1
