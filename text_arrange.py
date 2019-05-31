

input_file = r'D:\sunyt\projects\Img2Bits\text.c'
output_file = r'D:\sunyt\projects\Img2Bits\output.c'

with open(input_file, 'r') as f:
  text = f.readlines()

#print()
for y in range(2, len(text), 4):
  new0 = ''
  new1 = ''
  for x in range(0, len(text[y])-4, 10):
    new0 = new0 + text[y][x:x+5]
  for x in range(0, len(text[y+1])-4, 10):
    new0 = new0 + text[y+1][x:x+5]
  
  for x in range(5, len(text[y])-4, 10):
    new1 = new1 + text[y][x:x+5]
  for x in range(5, len(text[y+1])-4, 10):
    new1 = new1 + text[y+1][x:x+5]
  
  text[y] = new0 + '\n'
  text[y+1] = new1 + '\n'

with open(output_file, 'w') as f:
  f.writelines(text)

exit()

#####
_reverse = -1 if reverse_bit else 1
pic = Image.open('D:\sunyt\logo_anthony_12864_0.bmp')
p = np.array(pic)
p = np.int_(~p)
a = np.c_[p[0:8,:], p[8:16,:], p[16:24,:], p[24:32,:], p[32:40,:], p[40:48,:], p[48:56,:], p[56:64,:]]
b = a * pow(2, np.arange(8))[::_reverse].reshape(8,1)
c = np.sum(b, 0)

for line in c.reshape(64, 16):
  for e in line:
    print('0x%02X,' % e, end='')
  print()

