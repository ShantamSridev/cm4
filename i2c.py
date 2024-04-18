
import struct
import numpy as np  # Assuming usage of NumPy for the float array

def floats(byte_list):
    # Ensure the byte_list has the correct length
    if len(byte_list) != 32:
        raise ValueError("The list must be exactly 32 bytes long.")
    
    # Convert the list of integers into a bytes-like object
    bytes_obj = bytes(byte_list)
    
    # Convert every 4 bytes to a float and round it to 5 decimal places
    floats = [round(struct.unpack('f', bytes_obj[i:i+4])[0], 6) for i in range(0, len(bytes_obj), 4)]
    return floats


#rounds the values to 6 decimal places for compensating for IEEE 754 standard


def bytes_to_float_array(byte_list, float_array, float_array_index):
    """
    Convert bytes into floats and store them in a given NumPy float array starting from start_index.
    If two consecutive 0xFF bytes are found, stop processing further bytes.
    
    :param byte_list: List of bytes to be converted.
    :param array: NumPy array where the floats will be stored.
    :param start_index: Starting index in the array where the floats will be placed.
    """

    # Ensure the byte_list has the correct length
    if len(byte_list) != 32:
        raise ValueError("The list must be exactly 32 bytes long.")
    
    for i in range(0, len(byte_list), 4):
        # Check for the end marker (two consecutive 0xFF bytes)
        if byte_list[i:i+4].count(0xFF) >= 2:
            break  # Stop processing if end marker is found
        
        # Convert every 4 bytes to a float and round it to 5 decimal places
        rounded_float = round(struct.unpack('f', bytes(byte_list[i:i+4]))[0], 5)
        
        # Check if the index is within the range of the float_array
        if float_array_index < len(float_array):
            float_array[float_array_index] = rounded_float  # Store the float in the array
        else:
            # Expand the float_array if necessary
            float_array.append(rounded_float)
        
        # Increment the index for the next float
        float_array_index += 1
    
    return float_array

def send_i2c_command(bus, I2C_SLAVE_ADDRESS, mem_address, data):
    # Convert the list of floats to a byte array
    bytes_to_send = []

    for value in data:
        # Convert each float to 4 bytes in little-endian format
        float_bytes = struct.pack('=f',value)
        # Extend the byte array with these bytes
        bytes_to_send.extend(float_bytes)

    buf = bytes_to_send
    print(buf)
    try:
        bus.write_i2c_block_data(I2C_SLAVE_ADDRESS, mem_address, buf)
        print("Sent to",mem_address)
    except OSError:
        print("Couldn't write to slave, please check your wiring!")

def request_i2c_command(bus, I2C_SLAVE_ADDRESS, mem_address):

    try:
        block = bus.read_i2c_block_data(I2C_SLAVE_ADDRESS, mem_address, 32)
    except OSError:
        print("Couldn't read from slave")
        
    # Returned value is a list of 32 bytes
    #print(type(block))
    #print(block)
    new = []
    print(bytes_to_float_array(block,new,0))
