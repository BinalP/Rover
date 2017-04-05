import serial

ser = serial.Serial('/dev/ttyUSB0','9600')

while True:

	file = open('ser_data.txt','a')
		
	if ser.inWaiting():
		txt = ser.read()
		print txt
		file.write(txt+'\n')
	
	file.close()

	file = open('navigate.txt','r')

	txt = file.read()
	if txt == '\n':
		print 'No command found'
	else:
		ser.write(txt[0])
		print txt
	file.close()
