# Rigol-DP712-Examples
Basic examples on how to interface with a Rigol DP712 power supply

## General Notes
- To connect to this power supply you will need a USB to TTL cable. 
- - It's possible that you may need a NULL modem connector depending on the cable. This switches RX and TX
- By default the terminal configuration should be 9600 8N1. This can be confirmed by pressing the **SYSTEM** button on the front panel and navigating to the **Inter** menu using the arrow keys.
- Line feed is the termination character

[Scripts use PyVisa, read the docs here](https://pyvisa.readthedocs.io/en/latest/)

## Basic Commands
See the programming manual in the **Doc** folder for a full list of commands and descriptions. Below is a condensed table of the primary commands used in the examples

Command               | Description                                 | Response
--------------------- | ------------------------------------------- | --------
:MEASure?             | Measures output value in volts and displays | 0.000 when off. 
:OUTPut:STATe?        | Requests the current state of the output    | OFF or ON
:OUTPut:STATe CH1,ON <br />:OUTPut:STATe CH1,OFF | Turns the output ON and OFF                 | No response for the SET command
:APPLy CH1,30,2       | Sets the output to 30V and 2A               | No response for the SET command

## Scripts
### Demo.py - Hardcoded Example
Example with no adjustable parameters from the terminal. You'll need to manually adjust the COM port for this one to work. In this specific example the USB to RS232 cable on my computer is COM4.