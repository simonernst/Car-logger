#!/usr/bin/env python

import matplotlib.pyplot as plt
import csv
import statistics

""" 
class log_parser:

    def __init__(self):
        #open the file 
        #clean it if necessary

        #list file infos ncol, header


    def mean(self, list):
         """
#check if NULL bytes in file and erase them
f = open("log/car-2021-1-19-11-42-30.log", "rb")
raw_logfile = f.read()
f.close()
fo = open("log/car-2021-1-19-11-42-30.log", "wb")
fo.write(raw_logfile.replace('\x00', ''))
fo.close()



with open('log/car-2021-1-19-11-42-30.log', 'r') as logfile:
    has_header = csv.Sniffer().has_header(logfile.read(1024))
    
    #set csv config 
    delimiter = '\t'
    datatype = float

    logfile.seek(0)  # Rewind.

    #Read the logfile
    reader = csv.reader(logfile)

    #Get the number of columns in the file

    header = next(logfile)
    list_header = list(header.split(","))
    list_header = [x.strip(' ') for x in list_header]

    list_header[-1] = list_header[-1].strip()
    #print(list_header)
    
    ncol = len(next(reader))
    logfile.seek(0) # Rewind.
    if has_header:
        next(reader)  # Skip header row.

    dico = {}

    for i in range(0, ncol):
        #reset to line 1
        logfile.seek(0)
        next(reader)

        column = i 
        stuff = (datatype(row[column]) for row in reader)
        list_stuff = list(stuff)

        dico["{0}".format(list_header[i])] = list_stuff

    speed = dico['Speed']
    time = dico['Time']
    total_time = (max(time)-min(time))/60


    print("%.2f km/h" % statistics.mean(speed))

    print("%.2f minutes" % (total_time))

""" 
if __name__ == "__main__":
    #call class init 

 """









#open each logfile in the folder (except already treated file)

#create a specific folder for each file (will allow to check if file alredy parsed in a previous parsing )
#parse the log file


#create some fancy graphs

#output graph to file

#create a big graph with all graphs + car info + some calculated values
#e.g different mean values, vmax, rpm max, max acc, etc...
#time to reach hot engine (oil / coolant)





