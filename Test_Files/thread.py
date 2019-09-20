#-------------------------------------------------------------#
import timeit
import time # Use for time calls
from subprocess import call # Use for turning off the Pi
from threading import Thread
import os
start=timeit.default_timer()
# Creating the function generator
os.chdir("/home/pi/PiBits/ServoBlaster/user") # changing the directory to acces$
call("sudo ./servod --cycle-time=5000us --max=100% --min=0us", shell=True) # $
call("pwd", shell=True) # printing the current directory to make sure we've cha$
time.sleep(0.1)

ServoBlaster = open('/dev/servoblaster', 'w') # opening servoblaster

def func1(x):
    print('hi')
    ServoBlaster.write('%s' % (x))
    ServoBlaster.flush()
    print('out1')

x=['P1-12=200us' + '\n','P1-11=100us' + '\n']

for d in x:
    t=Thread(target=func1, args=(d,))
    t.start()

time.sleep(.01)

ServoBlaster.write('P1-11=0%' + '\n')
ServoBlaster.flush()
ServoBlaster.write('P1-12=0%' + '\n')
ServoBlaster.flush()
ServoBlaster.write('P1-15=0%' + '\n')
ServoBlaster.flush()

