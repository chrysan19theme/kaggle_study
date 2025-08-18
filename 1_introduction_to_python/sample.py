import re
import string

source='I wish I may, I wish I might Have a dish of fish tonight.'

print(re.findall(r'wish',source))
print(re.findall(r'wish|fish',source))
print(re.findall(r'^wish',source))
print(re.findall(r'^I wish',source))
print(re.findall(r'tonight\.$',source))
print(re.findall(r'[wf]ish',source))
print(re.findall(r'[wsh]+',source))
print(re.findall(r'ght\W',source))
print(re.findall(r'I (?=wish)',source))
print(re.findall(r'(?<=I) wish',source))