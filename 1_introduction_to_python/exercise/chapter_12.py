import re
import unicodedata
import binascii
import struct

#12.1
mystery='\U0001f984'
print(mystery)
print(unicodedata.name(mystery))

#12.2
pop_bytes=mystery.encode('utf-8')
print(pop_bytes)

#12.3
pop_string=pop_bytes.decode('utf-8')
print(pop_string)

#12.4
mammoth=''

#12.5
re.findall(r'\bc\w*',mammoth)

#12.6
re.findall(r'\bc\w[3]\b',mammoth)

#12.7
re.findall(r'\b\w*r\b',mammoth)

#12.8
re.findall(r'\b[^aeiou]*[aeiou]{3}[^aeiou]*\b',mammoth)

#12.9
hex_str='47494638396101000100080000000000ffffff21f90401000000002c000000000100010000020144003b'
gif=binascii.unhexlify(hex_str)
print(len(gif))

#12.10
print(gif[:6]==b'GIF89a')

#12.11
width,height=struct.unpack('<HH',gif[6:10])
print(width,height)