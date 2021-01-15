import obd
import time
from datetime import datetime
import os
import getpass

obd.logger.removeHandler(obd.console_handler)
class OBD_logger():
    def __init__(self, path):
        #Create log_files according to datetime
        print('Init')

        self.path = path


    def connect(self):

        while True:
            self.connection = obd.OBD()
            if not self.connection.is_connected():
                print("Failed to connect, will try again")
                time.sleep(5)
                break
            else:
                print("Connected")
                break

    def record(self):
        localtime = time.localtime(time.time())
        filename = self.path+"car-"+str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])+"-"+str(localtime[3])+"-"+str(localtime[4])+"-"+str(localtime[5])+".log"
        print('Start recording')
        with open(filename, "w", 128) as f:

            #Write the first line 
            f.write("%s, %s, %s, %s, %s, %s, %s, %s" % ("Time", "Speed", "RPM", "Cool_temp", "Intake_temp", "Load", "Ambiant air", "Baro pressure"))
            f.write("%s, %s, %s, %s, %s, %s, %s, %s" % ("Time", "Speed", "RPM", "Cool_temp", "Intake_temp", "Load", "Ambiant air", "Baro pressure"))

            while True:
                
                speed = self.connection.query(obd.commands.SPEED)
                rpm = self.connection.query(obd.commands.RPM)
                cool_temp = self.connection.query(obd.commands.COOLANT_TEMP)
                intake_temp = self.connection.query(obd.commands.INTAKE_TEMP)
                load = self.connection.query(obd.commands.ENGINE_LOAD)
                ambiant_air = self.connection.query(obd.commands.AMBIANT_AIR_TEMP)
                baro_pressure = self.connection.query(obd.commands.BAROMETRIC_PRESSURE)

                if not speed.is_null():
                    f.write("%d, %d, %d, %d, %d, %d, %d, %d" % (speed.time, speed.value, rpm.value, cool_temp.value, intake_temp.value, load.value, ambiant_air.value, baro_pressure.value))

        




if __name__=="__main__":
    
    logitems = ["RPM", "SPEED", "COOLANT_TEMP", "INTAKE_TEMP", "AMBIANT_AIR_TEMP", "ENGINE_LOAD", "BAROMETRIC_PRESSURE"]
    filepath = '/home/simon/test/project/log/'
    o = OBD_logger(filepath)
    o.connect()
    o.record()