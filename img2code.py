
from PIL import Image
import numpy as np
import struct

# config
reverse_bit = False

#####
_reverse = -1 if reverse_bit else 1
pic = Image.open('D:\sample.bmp')
p = np.array(pic)
p = np.int_(~p)
a = np.c_[p[0:8,:], p[8:16,:], p[16:24,:], p[24:32,:], p[32:40,:], p[40:48,:], p[48:56,:], p[56:64,:]]
b = a * pow(2, np.arange(8))[::_reverse].reshape(8,1)
c = np.sum(b, 0)

for line in c.reshape(64, 16):
  for e in line:
    print('0x%02X,' % e, end='')
  print()

