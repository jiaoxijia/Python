import struct
a = 200
b=400

str = struct.pack("ii",a,b)
print('length:',len(str))
print(str)
print(repr(str))

