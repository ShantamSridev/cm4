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

# while 1:
#     dat = [20.1]
#     mem_add = 0
#     #send_i2c_command(bus, slave_address, mem_add, dat)
#     request_i2c_command(bus, slave_address,mem_add)
#     time.sleep(2)  # Wait a bit for the slave to process

dat = [20.1]
mem_add = 4 # set_get_angle
send_i2c_command(bus, slave_address, mem_add, dat)
time.sleep(5)  # Wait a bit for the slave to process

mem_add = 16 #set_angle
dat = [180]
send_i2c_command(bus, slave_address, mem_add, dat)
time.sleep(5)

mem_add = 20 #set_angle
dat = [30]
send_i2c_command(bus, slave_address, mem_add, dat)
time.sleep(10)

mem_add = 20 #set_angle
dat = [0]
send_i2c_command(bus, slave_address, mem_add, dat)
time.sleep(5)
#mem_add = 8 #retreiving angle
#request_i2c_command(bus, slave_address,mem_add)
# time.sleep(5)  # Wait a bit for the slave to process

# mem_add = 16 #set_angle
# dat = [300]
# send_i2c_command(bus, slave_address, mem_add, dat)
# time.sleep(5)
# mem_add = 8 #retreiving angle
# request_i2c_command(bus, slave_address,mem_add)
# time.sleep(2)  # Wait a bit for the slave to process
# mem_add = 16 #set_angle
# dat = [10]
# send_i2c_command(bus, slave_address, mem_add, dat)
# time.sleep(5)
# mem_add = 8 #retreiving angle
# request_i2c_command(bus, slave_address,mem_add)
# time.sleep(2)  # Wait a bit for the slave to process
# mem_add = 16 #set_angle
# dat = [0]
# send_i2c_command(bus, slave_address, mem_add, dat)
# time.sleep(5)
# mem_add = 8 #retreiving angle
# request_i2c_command(bus, slave_address,mem_add)
# time.sleep(2)  # Wait a bit for the slave to process
