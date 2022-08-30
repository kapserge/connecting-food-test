from itertools import groupby
import csv
import datetime
from dateutil.parser import parse

def filetest():
    with open('small.csv') as csv_file:
        count =0
        reader = csv.reader(csv_file)
        next(reader) #skip header
     #Group by column (date)
        lst = sorted(reader, key=lambda x : (x[7], x[8]))
        #lsts = sorted(reader, key=lambda x : x[8])
        groups = groupby(lst, key=lambda x : x[7][:10])
        
     #Write file for each 
        for k,g in groups: 
            d= k.replace('-', '')
            groupss = groupby(lst, key=lambda x : x[8])
            for l, m in groupss:
                filename = d +"_"+ l + '.csv'
                with open(filename, 'w', newline='') as fout:
                    csv_output = csv.writer(fout)
                    csv_output.writerow(["producer_id","producer_name","product_id",
                                         "product_name","product_unit","quantity","specifications_id"
                                         ,"delivery_datetime","destination_country_code"])  #header
                    for line in m:
                        count =+1
                        if count  < 10000:
                             csv_output.writerow(line)
filetest()

