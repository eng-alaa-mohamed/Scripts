# This script is used to communicate with Resolute
# Input is port number and baud rate
# commands are already prefixed by $  use q to exit
# pip should be installed - Resolute is getting readings successfuly
import serial
import time

port = input("Enter port number COM" )
com_port = 'COM'+port
baud = input("Enter buadrate in bits/sec:")
ser = serial.Serial(port=com_port, baudrate=baud, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
if ser.isOpen():
    print(ser)
    time.sleep(1)

data_set = 4
data_list = [0]*data_set
def get_command ():
    data = ser.readline().decode('utf-8')
    return data

while True:
    data = ser.readline().decode('ascii')
    # print (data)
    log_file = open(r"F:\Git\Logs\log_2.log", "a")
    log_file.write(data)
    log_file.close()

    print(data)  #print the diagnostics
    command = '$' + input("Enter a command or 'q' to exit:$") + '\r\n'
	#command = input("Enter a command or 'q' to exit:") + '\r\n'
    if command == '$q\r\n':
	#if command == 'q\r\n':
         ser.close()
         exit ()
    else:
          ser.write(command.encode('utf-8'))
          for i in range (0, data_set):
              response = get_command()
              data_list[i] = response

              if response.find(command) != -1:
                  print("True")
                  print(data_list[i])
              break







