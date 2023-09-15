from tkinter import *
from tkinter import ttk, font
import time
import pyvisa

defaultVoltage = 12
defaultCurrent = 2

def measurePrint(seconds, my_instrument):
    startTime = time.time()
    currentTime = startTime

    while(currentTime-startTime < seconds):
        my_instrument.write(":MEASure?")
        print(my_instrument.read().rstrip()) # rstrip is to remove \n from the returned string
        currentTime = time.time()

def setFunction():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(Instrument_Target.get())    
    my_instrument.write(":APPLy CH1," + Voltage_Box.get() + "," + Current_Box.get())
    my_instrument.close()

def onFunction():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(Instrument_Target.get())    
    my_instrument.write(":OUTPut:STATe CH1,ON")
    my_instrument.close()

def offFunction():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(Instrument_Target.get())    
    my_instrument.write(":OUTPut:STATe CH1,OFF")
    my_instrument.close()

if __name__=="__main__":
    window = Tk()   
    window.geometry("350x235")
    window.title("Rigol DP712 Control Panel")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    mainframe = ttk.Frame(window, padding="10 10 10 10")
    mainframe.grid(column=0, row=0)

    ttk.Label(mainframe,text="Instrument",font=("Arial",16),width=10,justify=LEFT).grid(row=1,column=1)
    ttk.Label(mainframe,text="Voltage",font=("Arial",16),width=10,justify=LEFT).grid(row=2,column=1)
    ttk.Label(mainframe,text="Current",font=("Arial",16),width=10,justify=LEFT).grid(row=3,column=1)
    ttk.Label(mainframe,text=" ",font=("Arial",8),width=10,justify=LEFT).grid(row=4,column=1,columnspan=2)

    OPTIONS = pyvisa.ResourceManager().list_resources()
    Instrument_Target = StringVar(mainframe)
    Instrument_Target.set(OPTIONS[0])
    Instrument_Select = OptionMenu(mainframe, Instrument_Target, *OPTIONS)
    Instrument_Select.grid(row=1, column=2)

    Voltage_Box = Entry(mainframe, width=10, font=("Arial", 16))
    Voltage_Box.grid(row=2, column=2)
    Voltage_Box.insert(0,defaultVoltage)

    Current_Box = Entry(mainframe, width=10, font=("Arial", 16))
    Current_Box.grid(row=3, column=2)
    Current_Box.insert(0,defaultCurrent)

    f = font.Font(weight="bold",size=18,family="Arial")
    Set_button = Button(mainframe, text="SET", command=setFunction,width=20,bg="blue",fg="white",activebackground="white",activeforeground="blue")
    Set_button['font'] = f
    Set_button.grid(row=5,column=1,columnspan=2)

    f = font.Font(weight="bold",size=18,family="Arial")
    Set_button = Button(mainframe, text="ON", command=onFunction,width=8,bg="green",fg="white",activebackground="white",activeforeground="green")
    Set_button['font'] = f
    Set_button.grid(row=6,column=1, padx=0, pady=0, sticky=NSEW)

    f = font.Font(weight="bold",size=18,family="Arial")
    Set_button = Button(mainframe, text="OFF", command=offFunction,width=8,bg="red",fg="white",activebackground="white",activeforeground="red")
    Set_button['font'] = f
    Set_button.grid(row=6,column=2,columnspan=2, padx=0, pady=0, sticky=NSEW)

    mainloop()