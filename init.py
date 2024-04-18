import smbus
import time
import struct
import i2c
from i2c import bytes_to_float_array
from i2c import send_i2c_command
from i2c import request_i2c_command
import RPi.GPIO as GPIO

# Set up the I2C bus and slave address
bus = smbus.SMBus(1)  # Check your bus number
slave_address = 0x23  # Change to your slave's address

MOSFETPin = 12

GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setwarnings(False)
GPIO.setup(MOSFETPin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(MOSFETPin, GPIO.HIGH)
