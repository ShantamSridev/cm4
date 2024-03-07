import smbus
import time
import struct

# Set up the I2C bus and slave address
bus = smbus.SMBus(1)  # Check your bus number
slave_address = 0x17  # Change to your slave's address

# Function to send messages to the slave
def send_to_slave(data):
    bus.write_i2c_block_data(slave_address, 0x20, data)

# Function to request data from the slave
def request_from_slave():
    return bus.read_i2c_block_data(slave_address, 0x20, 32)

# Send a 5-byte command/message to the slave


# # Request 32 bytes of data from the slave
# received_data = request_from_slave()
# print("Received from slave:", received_data)


def send_i2c_command(bus, I2C_SLAVE_ADDRESS, mem_address, data):
    # Convert float to 4-byte array
    #float_bytes = struct.pack('f', data)

    # Prepare the buffer
    # Note: When transmitting over I2C, we usually don't send floats directly as text
    # Instead, we send them as binary data
    
    #buf = [mem_address] + data
    # write message at mem_address
    #buf = [5,21.1]

    # Convert the list of floats to a byte array
    bytes_to_send = []

    # add = struct.pack("=i", mem_address)
    # bytes_to_send.extend(add)

    for value in data:
        # Convert each float to 4 bytes in little-endian format
        float_bytes = struct.pack('=f',value)
        # Extend the byte array with these bytes
        bytes_to_send.extend(float_bytes)


    #buf = mem_address + bytes_to_send
    buf = bytes_to_send
    #print(f"Write at 0x{mem_address:02X}: '{data}'")
    print(buf)
    try:
        bus.write_i2c_block_data(slave_address, mem_address, buf)
    except OSError:
        print("Couldn't write to slave, please check your wiring!")


while 1:
    message = [0x02, 0x03, 0x04, 0x08]  # Sample data
    dat = [20.1]
    mem_add = 5
    send_i2c_command(bus, slave_address, mem_add, dat)
    time.sleep(2)  # Wait a bit for the slave to process
