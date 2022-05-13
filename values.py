#!/usr/bin/python3
import sys
head='''
<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />

<title>Colors</title>

</head>
<body style="background:#6A6C6E">'''
end='''
</body>
</html>'''
cols = []
incol=sys.argv[1]

#get colors from arg
inred=int('0x'+incol[0:2],16)
cols.append(inred)
ingreen=int('0x'+incol[2:4],16)
cols.append(ingreen)
inblue=int(incol[4:],16)
cols.append(inblue)
#ort colors
cols_sorted = cols.copy()
cols_sorted.sort()
#print(hex(cols_sorted[0]),hex(cols_sorted[1]),hex(cols_sorted[2]))
high = cols_sorted[2]
mid = cols_sorted[1]
low = cols_sorted[0]
#print(red_idx,green_idx,blue_idx)
#sys.exit()

#set h_col, m_col and l_col 

if high == cols[0]:
    h_col = 'red'
elif high == cols[1]:
    h_col = 'green'
elif high == cols[2]:
    h_col = 'blue'
if mid == cols[0]:
    m_col = 'red'
elif mid == cols[1]:
    m_col = 'green'
elif mid == cols[2]:
    m_col = 'blue'
if low == cols[0]:
    l_col = 'red'
elif low == cols[1]:
    l_col = 'green'
elif low == cols[2]:
    l_col = 'blue'

# we need higher shades, and lower shades
# we will produce ten shades, including niput color
num_higher_shades = 0
num_lower_shades = 0

position = high/256 * 100
#print(position) 

if position > 90:
        num_higher_shades = 0
        num_lower_shades = 9 
elif position > 80:
        num_higher_shades = 1
        num_lower_shades = 8 
elif position > 70:
        num_higher_shades = 2
        num_lower_shades = 7 
elif position > 60:
        num_higher_shades = 3
        num_lower_shades = 6 
elif position > 50:
        num_higher_shades = 4
        num_lower_shades = 5 
elif position > 40:
        num_higher_shades = 5
        num_lower_shades = 4 
elif position > 30:
        num_higher_shades = 6
        num_lower_shades = 3 
elif position > 20:
        num_higher_shades = 7
        num_lower_shades = 2 
elif position > 10:
        num_higher_shades = 8
        num_lower_shades = 1 
elif position > 0:
        num_higher_shades = 9
        num_lower_shades = 0 

#print('higher shades',num_higher_shades)
#print('lower shares',num_lower_shades)

#h2l and h2m are the ratios of the high color to 
#the low color and the medium col
h2l = cols[0]/cols[1]
h2m = cols[0]/cols[2]

print(head)

# print lower shades (less light)
idx = 0

lowers = []
_high = high
while idx < num_lower_shades:
    idx += 1
    _high = _high - 25
    _mid = int(_high/h2m)
    _low = int(_high/h2l)
    #print(str(hex(_high))[2:],str(hex(_mid))[2:],str(hex(_low))[2:])
    if _high < 0 or _mid < 0 or _low <0: break
    _col = '#'
    if _high < 16: _col += '0'
    if h_col == 'red':
        _col += str(hex(_high))[2:]
    if h_col == 'green':
        _col += str(hex(_high))[2:]
    if h_col == 'blue':
        _col += str(hex(_high))[2:]
    if _mid < 16: _col += '0'
    if m_col == 'red':
        _col += str(hex(_mid))[2:]
    if m_col == 'green':
        _col += str(hex(_mid))[2:]
    if m_col == 'blue':
        _col += str(hex(_mid))[2:]
    if _low < 16: _col += '0'
    if l_col == 'red':
        _col += str(hex(_low))[2:]
    if l_col == 'green':
        _col += str(hex(_low))[2:]
    if l_col == 'blue':
        _col += str(hex(_low))[2:]
    lowers.append('<div style="background:{}"><h1>MB {}</h1></div>'.format(_col,_col))
    #print('<div style="background:{}"><h1>MB {}</h1></div>'.format(_col,_col))

for i, x in reversed(list(enumerate(lowers))):
    print(x)

#add base color
col='#'+str(hex(inred))[2:4]+str(hex(ingreen))[2:4]+str(hex(inblue))[2:4]
#print(col)
print('<div style="background:{}"><h1> BASE {}</h1></div>'.format(col,col))

idx = 0 
_high = high
# print higher shades (more light)
while idx < num_higher_shades:
    idx += 1
    _high = _high + 25
    _mid = int(_high/h2m)
    _low = int(_high/h2l)
    #print(str(hex(_high))[2:],str(hex(_mid))[2:],str(hex(_low))[2:])
    _col = '#'
    if _high < 16: _col += '0'
    if h_col == 'red':
        _col += str(hex(_high))[2:]
    if h_col == 'green':
        _col += str(hex(_high))[2:]
    if h_col == 'blue':
        _col += str(hex(_high))[2:]
    if _mid < 16: _col += '0'
    if m_col == 'red':
        _col += str(hex(_mid))[2:]
    if m_col == 'green':
        _col += str(hex(_mid))[2:]
    if m_col == 'blue':
        _col += str(hex(_mid))[2:]
    if _low < 16: _col += '0'
    if l_col == 'red':
        _col += str(hex(_low))[2:]
    if l_col == 'green':
        _col += str(hex(_low))[2:]
    if l_col == 'blue':
        _col += str(hex(_low))[2:]
    #print(_col)
    print('<div style="background:{}"><h1>MB {}</h1></div>'.format(_col,_col))

print(end)

sys.exit()


