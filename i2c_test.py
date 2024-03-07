import smbus
import time
import struct

# Set up the I2C bus and slave address
bus = smbus.SMBus(1)  # Check your bus number
slave_address = 0x17  # Change to your slave's address


def send_i2c_command(bus, I2C_SLAVE_ADDRESS, mem_address, data):
    # Convert the list of floats to a byte array
    bytes_to_send = []

    for value in data:
        # Convert each float to 4 bytes in little-endian format
        float_bytes = struct.pack('=f',value)
        # Extend the byte array with these bytes
        bytes_to_send.extend(float_bytes)

    buf = bytes_to_send
    print("Sent to",mem_address)
    print(buf)
    try:
        bus.write_i2c_block_data(slave_address, mem_address, buf)
    except OSError:
        print("Couldn't write to slave, please check your wiring!")

def request_i2c_command(bus, I2C_SLAVE_ADDRESS, mem_address):

    try:
        block = bus.read_i2c_block_data(slave_address, mem_address, 32)
    except OSError:
        print("Couldn't read from slave")
        
    # Returned value is a list of 32 bytes
    print(block)


while 1:
    dat = [20.1]
    mem_add = 5
    send_i2c_command(bus, slave_address, mem_add, dat)
    request_i2c_command(bus, slave_address,mem_add)
    time.sleep(2)  # Wait a bit for the slave to process
