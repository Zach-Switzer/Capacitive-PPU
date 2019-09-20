
#-------------------------------------------------------------#
import timeit
import time # Use for time calls
from subprocess import call # Use for turning off the Pi
from multiprocessing import Process
import os
start=timeit.default_timer()
# Creating the function generator
os.chdir("/home/pi/PiBits/ServoBlaster/user") # changing the directory to acces$
call("sudo ./servod --cycle-time=5000us --max=100% --min=0us", shell=True) # $
call("pwd", shell=True) # printing the current directory to make sure we've cha$
time.sleep(0.1)

ServoBlaster = open('/dev/servoblaster', 'w') # opening servoblaster

def func1():
    print('hi')
    ServoBlaster.write('P1-16=100us' + '\n')
    ServoBlaster.flush()
    print('out1')


def func2():
    time.sleep(.0006)
    print('hi2')
    ServoBlaster.write('P1-15=200us' + '\n')
    ServoBlaster.flush()
    print('out2')

if __name__== '__main__':
    p1=Process(target=func1)
    p1.start()
    p2=Process(target=func2)
    p2.start()
    p1.join()
    p2.join()


time.sleep(.1)

ServoBlaster.write('P1-11=0%' + '\n')
ServoBlaster.flush()
ServoBlaster.write('P1-12=0%' + '\n')
ServoBlaster.flush()
ServoBlaster.write('P1-15=0%' + '\n')
ServoBlaster.flush()
ServoBlaster.write('P1-16=0%' + '\n')
ServoBlaster.flush()

# will not pass 3 inputs simultaneously


