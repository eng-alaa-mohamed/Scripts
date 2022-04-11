#!/usr/bin/env python3
import argparse
import serial
import time
import io
import datetime
import os

parser = argparse.ArgumentParser(
                 description='Description of the program' )
parser.add_argument( 'comPort', type=str, help='COM Port of the GeoPin (COMx or /dev/ttyUSBX)' )
parser.add_argument( '-b','--baud', action='store', type=int, required=False,
                    help='BAUD rate of the Geopin, defaults to 115200',
                    default='115200' )
parser.add_argument(  '-f','--flow', action='store_true',
					help='If enabled, flow control is set to enabled, default to disabled')
args = parser.parse_args()

now = datetime.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string_stripped = now.strftime("%d%m%Y_%H%M%S")

ser = serial.Serial(port = args.comPort,baudrate = str(args.baud),timeout=0.1)
 
print("Connected to: " + ser.portstr)
filename="output_"+ dt_string_stripped + ".bin"
f = open(filename, "ab")

# Rotate the bin daily on a message boundary
while True:
	s = ser.read(1024)
	f.write(s)
	f.flush()