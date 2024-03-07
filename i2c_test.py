# Test for i2c communications with a Raspberry Pi Pico
import smbus
from time import sleep
import struct

# I2C channel 1 is connected to the GPIO pins
channel = 1
# Address of the peripheral device
address = 0x17

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

i=1000


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
    buf = [mem_address] + list(bytes_to_send)
    #print(f"Write at 0x{mem_address:02X}: '{data}'")
    print(buf)
    try:
        bus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0, buf)
    except OSError:
        print("Couldn't write to slave, please check your wiring!")



while 1:
    print ("Start loop "+str(i))
    sleep (2)
    mem_add = 5
    data = [20.1]

    send_i2c_command(bus, address, mem_add, data)

    # try:
    #     print ("Writing data "+str(i))
    #     # Write out I2C command: address, cmd, msg[0]
    #     bus.write_i2c_block_data(address, i&0xff, [i>>8])
    # except Exception as e:
    #     print ("Writing Error "+str(e))
    #     continue
    # #sleep (0.1)
    # read = 0
    # while read == 0:
    #     try:
    #         print ("Reading data")
    #         rx_bytes = bus.read_i2c_block_data(address, 0, 2) # where zero is the memory address 
    #     except Exception as e:
    #         print ("Read Error "+str(e))
    #         continue
    #     read = 1
    # print ("Read "+str(rx_bytes))
    # value = rx_bytes[0] + (rx_bytes[1] << 8)
    # print ("Read value "+str(value))
    i+=1
    



# # Prepare the message
# msg = "Hello, I2C slave! - 0x{:02X}".format(mem_address)
# msg_len = len(msg)

# # Prepare the buffer
# buf = [mem_address] + list(msg.encode())  # converting message to list of byte values

# # write message at mem_address
# print(f"Write at 0x{mem_address:02X}: '{msg}'")
# try:
#     bus.write_i2c_block_data(I2C_SLAVE_ADDRESS, buf[0], buf[1:1 + msg_len])
# except OSError:
#     print("Couldn't write to slave, please check your wiring!")
#     continue

# # No direct equivalent in Python for hard_assert, but we can raise an exception for a false condition
# # Here, the verification of the write length can be complex as Python SMBus does not return the count directly.
# # For simplicity, we'll assume successful write if no exception was raised.

# # seek to mem_address (repeated start condition in Python SMBus is handled internally)
# try:
#     bus.write_byte(I2C_SLAVE_ADDRESS, buf[0])
# except OSError:
#     print("Error setting memory address.")
#     exit()

# # Partial read
# split = 5
# read_back = bus.read_i2c_block_data(I2C_SLAVE_ADDRESS, buf[0], split)
# assert len(read_back) == split, "Read length mismatch"
# print(f"Read  at 0x{mem_address:02X}: '{bytes(read_back).decode()}'")
# assert read_back == buf[1:1 + split], "Data mismatch"

# # Read the remaining bytes, continuing from last address
# remaining = bus.read_i2c_block_data(I2C_SLAVE_ADDRESS, buf[0] + split, msg_len - split)
# assert len(remaining) == msg_len - split, "Read length mismatch"
# print(f"Read  at 0x{mem_address + split:02X}: '{bytes(remaining).decode()}'")
# assert remaining == buf[1 + split:1 + msg_len], "Data mismatch"

# print("")
# sleep(2)  # sleep for 2000 milliseconds


# def receive_i2c_block(bus, I2C_SLAVE_ADDRESS, mem_address):
#     try:
#         bus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0, mem_address)
#     except OSError:
#         print("Couldn't write address for receive to slave")
#         continue

#     #partial read code
