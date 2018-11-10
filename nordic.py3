import serial
import sys

def setupSerial(port_name):
	serial_port = serial.Serial(port_name)
	serial_port.baudrate = 115200
	serial_port.timeout = 1
	return serial_port

def sendString(serial_object, text):
	return serial_object.write(text)

def getString(serial_object):
	nrf52_ret = serial_object.read(2000)
	return nrf52_ret

def issueCMD(serial_object, text):
	sendString(serial_object, text)
	retext = getString(serial_object)
	return retext

def drawArt(art):
	'''
	Do some magic and draw beautiful ASCII art
	'''
	art_lines = art.decode("utf-8").split("\r\n")
	for line in art_lines[1:-3]:
		print(line)
	print(art_lines[-3][7:])

def main(arguments):
	'''
	Connect to nRF52 DK through serial port and print the "Nordic"-logo
	'''
	argument = arguments[1]
	serial_port = 'COM7'
	ser = setupSerial(serial_port)
	if argument == 'art':
		command = 'nordic\r\n'.encode() # encode as byte array
		art = issueCMD(ser, command)
		drawArt(art)
	elif argument == 'led':
		command = 'python\r\n'.encode()
		issueCMD(ser, command)
	else:
		print("{} is an unknown argument.".format(argument))

	ser.close()


if __name__ == '__main__':
	print ('Number of arguments:', len(sys.argv), 'arguments.')
	print ('Argument List:', str(sys.argv))
	main(sys.argv)