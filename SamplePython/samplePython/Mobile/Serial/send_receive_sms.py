import time
import serial

recipient = "085220902022"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyUSB0",  9600, timeout=5)

time.sleep(0.5)
phone.write(b'AT\r')
msg=phone.read(64)
print(msg)

time.sleep(0.5)
phone.write(b'AT+CMGF=1\r')
msg=phone.read(64)
print(msg)
"""
#Mengirim Pesan
time.sleep(0.5)
phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
msg=phone.read(64)
print(msg)

time.sleep(0.5)
phone.write(message.encode() + b"\r")
msg=phone.read(64)
print(msg)

time.sleep(0.5)
phone.write(bytes([26]))
msg=phone.read(64)
print(msg)
"""
#Menerima Persan
time.sleep(0.5)
phone.write(b'AT+CMGL="ALL"\r')
msg=phone.read(64)
print(msg)


time.sleep(0.5)
phone.close()