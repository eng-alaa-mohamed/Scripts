import serial
import time
from xbee import XBee, ZigBee

port = input ("Enter port number:" )
baud = input ("Enter buadrate in bits/sec:" )
ser = serial.Serial (port, baud, timeout=1)
time.sleep(1)
if ser.isOpen():
     print(port + ' is open...')

# Set the NI string of the radio
xbee = XBee(ser)
xbee.atcmd("NI", "Rover_33")  #NI = Rover_3
xbee.atcmd("CH", 0x46)   #CH =F
#xbee.atcmd("DL", b'\x12\x25\x89\xF5')  # Bytes


time.sleep(1)
xbee.at(command='WR') # parameter in Hex
print ("Done")
time.sleep(1)
xbee.at(command='FR') # Command to Reset the Xbee
time.sleep(1)
ser.close()

