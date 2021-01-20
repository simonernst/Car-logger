import obd
import time
from datetime import datetime
import os
import getpass

obd.logger.removeHandler(obd.console_handler)
class OBD_logger():
    def __init__(self, path):
        self.path = path

    def connect(self):

        while True:
            self.connection = obd.OBD()
            if not self.connection.is_connected():
                print("Failed to connect, will try again")
                time.sleep(5)
            else:
                print("Connected")
                break

    def record(self):

        localtime = time.localtime(time.time())
        filename = self.path+"car-"+str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])+"-"+str(localtime[3])+"-"+str(localtime[4])+"-"+str(localtime[5])+".log"   
        list_ukn, list_pid, list_all = [], [], []

        #Get all the PID commands supported by the car
        supported_commands = self.connection.supported_commands

        #Reads the supported commands and parse them into 3 categories
        for c in supported_commands:
            if c.ecu == 1:
                list_ukn.append(c.name)
            elif c.ecu == 2 and "PID" not in c.name:
                list_pid.append(c.name)
            else:
                list_all.append(c.name)

    
        if(len(list_pid) == 0):
            print("No pid 01 commands are supported, abort...")
            self.connection.close()
            return

        #Opens the logfile to write all the relevant infos in it
        with open(filename, "w", 128) as f:

            #TODO: check how DTCs are returned and find a way to store it in csv
            """
            #Read the DTCs on the car 
            dtc = self.connection.query(obd.commands["GET_DTC"])
            if not dtc.is_null():
                f.write("DTC: %s \n" % dtc.value.magnitude)
            """
            #Read the VIN of the car
            try:
                vin = self.connection.query(obd.commands["VIN"])          
                if not vin.is_null():
                    f.write("VIN: %s \n" % vin.value.magnitude)
            except:
                f.write("VIN: unknown\n")

            #Read the fuel type
            if "FUEL_TYPE" in list_pid:
                fuel = self.connection.query(obd.command["FUEL_TYPE"])
                f.write("Fuel type: %s \n" % fuel.value.magnitude)
            else: 
                f.write("Fuel type: unknown \n")

            f.write("Time, ")
            for element in list_pid:
                f.write(str(element))
                if element != list_pid[-1]:
                    f.write(',')
                else:
                    f.write('\n')

                speed = self.connection.query(obd.commands[element])


            #TODO : add car info at the beginning of the log file
            #e.g car model, DTCs, fuel type

            print('Start recording...')
            while True:
                f.write("%d," % self.connection.query(obd.commands[list_pid[0]]).time)

                for element in list_pid:                    
                    f.write("%d" % self.connection.query(obd.commands[element]).value.magnitude)
                    if element != list_pid[-1]:
                        f.write(',')
                    else:
                        f.write('\n')


if __name__=="__main__":
    
    
    
    #TODO : change filepath to username + current_directory
    #TODO : add path check
    filepath = '/home/simon/207-logger/log/'
    o = OBD_logger(filepath)
    o.connect()
    o.record()