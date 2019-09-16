#-------------------------------------------------------------#
import timeit
import time # Use for time calls
from subprocess import call # Use for turning off the Pi
import sys, select # Use for timed user input
import os
start=timeit.default_timer()
# Creating the function generator
os.chdir("/home/pi/PiBits/ServoBlaster/user") # changing the directory to acces$
call("sudo ./servod --cycle-time=5000us --max=100% --min=0us", shell=True) # $
call("pwd", shell=True) # printing the current directory to make sure we've cha$
time.sleep(0.1)

ServoBlaster = open('/dev/servoblaster', 'w') # opening servoblaster

# Turn on the IGBT to charge the inductor
for i in range (0,4):
    ServoBlaster.write('P1-12=600us' + '\n') # pulse width of 200us
    ServoBlaster.flush()
    #ServoBlaster.write('P1-15=0%' + '\n') # pulse width of 200us
    #ServoBlaster.flush()
    print('Inductor pulsing!')
    time.sleep(.005)

ServoBlaster.write('P1-12=0%' + '\n')
ServoBlaster.flush()
#print('turning off pin 12')
time.sleep(.005)
print(timeit.default_timer()-start)

# Release the capacitors
start1=timeit.default_timer()
ServoBlaster.write('P1-11=100%' + '\n')
ServoBlaster.flush()
print(timeit.default_timer()-start1)
print(timeit.default_timer()-start)
start2=timeit.default_timer()
time.sleep(.0001)
ServoBlaster.write('P1-15=100%' + '\n')
ServoBlaster.flush()
print(timeit.default_timer()-start2)
print(timeit.default_timer()-start1)
print(timeit.default_timer()-start)
start3=timeit.default_timer()
time.sleep(.0001)
ServoBlaster.write('P1-16=100%' + '\n')
ServoBlaster.flush()
print(timeit.default_timer()-start3)
print(timeit.default_timer()-start1)
print(timeit.default_timer()-start)
start4=timeit.default_timer()
time.sleep(.0001)
ServoBlaster.write('P1-18=100%' + '\n')
ServoBlaster.flush()
print(timeit.default_timer()-start4)
print(timeit.default_timer()-start1)
print(timeit.default_timer()-start)
start5=timeit.default_timer()
time.sleep(1)
print(timeit.default_timer()-start5)

# Close the capacitors
ServoBlaster.write('P1-11=0%' + '\n')
ServoBlaster.flush()
#time.sleep(0.01)
ServoBlaster.write('P1-15=0%' + '\n')
ServoBlaster.flush()
#time.sleep(0.01)
ServoBlaster.write('P1-16=0%' + '\n')
ServoBlaster.flush()
#time.sleep(0.01)
ServoBlaster.write('P1-18=0%' + '\n')
ServoBlaster.flush()
#time.sleep(0.1)


