import time
import pyvisa

def measurePrint(seconds):
    startTime = time.time()
    currentTime = startTime

    while(currentTime-startTime < seconds):
        my_instrument.write(":MEASure?")
        print(my_instrument.read().rstrip()) # rstrip is to remove \n from the returned string
        currentTime = time.time()


# Connect, print list of available resources and instrument
rm = pyvisa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('ASRL4::INSTR') # COM4 on my computer
print(my_instrument.query('*IDN?'))              # Display instrument info

# Set our instrument to 30V and 2A
my_instrument.write(":APPLy CH1,30,2")

measurePrint(1)
my_instrument.write(":OUTPut:STATe CH1,ON")
measurePrint(2)
my_instrument.write(":OUTPut:STATe CH1,OFF")
measurePrint(1)      