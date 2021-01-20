#!/usr/bin/env python

import matplotlib as mpl
mpl.use('Agg')
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
f = open("log/car-2021-1-19-11-42-30.log", "r")
raw_logfile = f.read()
f.close()
fo = open("log/car-2021-1-19-11-42-30.log", "w")
fo.write(raw_logfile.replace('\x00', ''))
fo.close()



with open('log/car-2021-1-19-11-42-30.log', 'r', newline="\n") as logfile:
    has_header = csv.Sniffer().sniff(logfile.readline())
    
    #set csv config 
    delimiter = '\t'
    datatype = float

    logfile.seek(0)  # Rewind.

    
    reader = csv.reader(logfile) #Read the logfile

    #Get the header variables and remove whitespaces
    header = next(logfile)
    list_header = list(header.split(","))
    list_header = [x.strip(' ') for x in list_header]
    list_header[-1] = list_header[-1].strip()

    #Get the number of columns in the log file   
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
    start_time = time[0]
    print(start_time)

    #Set first time value to 0
    dico['Time'] = [x - time[0] for x in dico['Time']]
    time = dico['Time']
    start_time = time[0]
    print(start_time)

    load=dico['Load']
    total_time = (max(time)-min(time))/60
    rpm = dico['RPM']
    cool_temp = dico['Cool_temp']

    print("Vitesse moyenne: %.2f km/h" % statistics.mean(speed))
    print("Vitesse maximale: %.2f km/h" % max(speed))
    print("Regime moteur max: %d" % max(rpm))
    print("Temps de trajet: %.2f minutes" % (total_time))

    #Plot tests

    fig = plt.figure()
    #fig.set_title("Some data from my car")
    
    
    ax = fig.add_subplot(221)
    ax.plot(time, speed)
    ax2 = fig.add_subplot(222)
    ax2.plot(time, load)
    ax3 = fig.add_subplot(223)
    ax3.plot(time,cool_temp)
    ax4 = fig.add_subplot(224)
    ax4.plot(time,rpm)

    ax.set_title('Vitesse')
    ax2.set_title('Charge moteur')
    ax3.set_title('Temp liquide de refroidissement')
    ax4.set_title('Vitesse moteur')


    ax.set_xlabel('time (second)')
    ax2.set_xlabel('time (second)')
    ax3.set_xlabel('time (second)')
    ax4.set_xlabel('time (second)')

    ax.set_ylabel('Vitesse (km/h)')
    ax2.set_ylabel('charge (%)')
    ax3.set_ylabel('T coolant (C)')
    ax4.set_ylabel('Rpm (Tr/min)')
    fig.set_size_inches(18.5, 10.5)   
    fig.savefig('temp.png', dpi=200)



#TODO : change to class 
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





