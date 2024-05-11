from zlib import crc32
 
file_name = input('Enter the file name: ')
data = open(file_name, 'rb').read()
index = 12  
IHDR = bytearray(data[index:index + 17])  
width_index = 7  
height_index = 11  
target_crc = input('Enter 4-byte crc32 value: ')
target_crc = int(target_crc, 16)
 
for width in range(1, 2000):
    width_bytes = bytearray(width.to_bytes(2, 'big'))
 
    for height in range(1, 2000):
        height_bytes = bytearray(height.to_bytes(2, 'big'))
 
        for i in range(len(height_bytes)):
            IHDR[height_index - i] = height_bytes[-i - 1]
        for i in range(len(width_bytes)):
            IHDR[width_index - i] = width_bytes[-i - 1]
 
        current_crc = crc32(IHDR) & 0xFFFFFFFF  
        if current_crc == target_crc:
            print("width: {}, height: {}"
                  .format(hex(width)[2:].upper(), hex(height)[2:].upper()))
            break
    else:
        continue 
    break 
 
