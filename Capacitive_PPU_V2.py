#-------------------------------------------------------------#
#--------- Code for Matrix thruster w/ Capcitive PPU ---------#
#-------------------------------------------------------------#

import timeit
import time # Use for time calls
from subprocess import call # Use for turning off the Pi
import sys, select # Use for timed user input
import os

# Creating the function generator
os.chdir("/home/pi/PiBits/ServoBlaster/user") # changing the directory to access the servod.c file
call("sudo ./servod --cycle-time=200000us --max=100% --min=0us", shell=True) # editing the servod.c file
call("pwd", shell=True) # printing the current directory to make sure we've changed directories
time.sleep(0.1)

ServoBlaster = open('/dev/servoblaster', 'w') # opening servoblaster

while (KeyboardInterrupt!=True): # while loops that runs until you stop it
    # Turn on the IGBT to charge the inductor
    t1=time.time()
    for i in range (0,18):
        ServoBlaster.write('P1-12=200us' + '\n') # pulse width of 200us
        ServoBlaster.flush()
        print('Inductor pulsing!')
        time.sleep(.2)

    # Take time data & turn off the pulsing to the inductor
    ServoBlaster.write('P1-12=0%' + '\n')
    ServoBlaster.flush()
    print('This is the code execution time: '+str(timeit.timeit('char in text', setup='text = "sample string"; char = "g"')))
    t2=time.time()
    print(t2-t1)
    print('turning off pin 12')
    time.sleep(1)

    # Release the capacitors
    ServoBlaster.write('P1-13=100%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.5)
    ServoBlaster.write('P1-15=100%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.5)
    ServoBlaster.write('P1-16=100%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.5)
    ServoBlaster.write('P1-18=100%' + '\n')
    ServoBlaster.flush()
    time.sleep(2)

    # Close the capacitors
    ServoBlaster.write('P1-13=0%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.1)
    ServoBlaster.write('P1-15=0%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.1)
    ServoBlaster.write('P1-16=0%' + '\n')
    ServoBlaster.flush()
    time.sleep(0.1)
    ServoBlaster.write('P1-18=0%' + '\n')
    ServoBlaster.flush()
    time.sleep(2)
