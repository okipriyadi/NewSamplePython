import serial
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)
cmd='AT+CMGL=?\r'
ser.write(cmd.encode())
msg=ser.read(64)
print(msg)