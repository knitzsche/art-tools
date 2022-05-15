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

cols_sorted = cols.copy()
cols_sorted.sort()
#print(hex(cols_sorted[0]),hex(cols_sorted[1]),hex(cols_sorted[2]))
high = cols_sorted[2]
mid = cols_sorted[1]
low = cols_sorted[0]

#set h_col, m_col and l_col 
ranks = {}
if high == cols[0]:
    h_col = 'red'
    ranks['high'] = 'red'
    if mid == cols[1]:
        m_col = 'green'
        ranks['mid'] = 'green'
        l_col='blue'
        ranks['low'] = 'blue'
    else:
        m_col = 'blue'
        ranks['mid'] = 'blue'
        l_col = 'green'
        ranks['low'] = 'green'

if high == cols[1]:
    h_col = 'green'
    ranks['high'] = 'green'
    if mid == cols[0]:
        m_col = 'red'
        ranks['mid'] = 'red'
        l_col='blue'
        ranks['low'] = 'blue'
    else:
        m_col = 'blue'
        ranks['mid'] = 'blue'
        l_col = 'red'
        ranks['low'] = 'red'

if high == cols[2]:
    h_col = 'blue'
    ranks['high'] = 'blue'
    if mid == cols[0]:
        m_col = 'red'
        ranks['mid'] = 'red'
        l_col='green'
        ranks['low'] = 'green'
    else:
        m_col = 'green'
        ranks['mid'] = 'green'
        l_col = 'red'
        ranks['low'] = 'red'

# we need number of higher shades, and lower shades
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
h2l = cols_sorted[2]/cols_sorted[0]
h2m = cols_sorted[2]/cols_sorted[1]
print(head)

# print lower shades (less light)
idx = 0
#print("<h2>High: {} Mid {} Low {}</h2>".format(h_col, m_col, l_col))
lowers = []
_high = high
while idx < num_lower_shades:
    idx += 1
    _high = _high - 25
    _mid = int(_high/h2m)
    _low = int(_high/h2l)
    #print(str(hex(_high))[2:],str(hex(_mid))[2:],str(hex(_low))[2:])

    _h = ''
    _m = ''
    _l = '' 
    _col = '#'
    if _high < 16: _h = '0' + str(hex(_high))[2:]
    else: _h = str(hex(_high))[2:]
    if _mid < 16: _m = '0' + str(hex(_mid))[2:]
    else: _m = str(hex(_mid))[2:]
    if _low < 16: _l = '0' + str(hex(_low))[2:]
    else: _l = str(hex(_low))[2:]
    if ranks['high'] == 'red':
        _col += _h
        if ranks['mid'] == 'green':
            _col += _m
            _col += _l
        else:
            _col += _l
            _col += _m
    elif ranks['mid'] == 'red':
        _col += _m
        if ranks['high'] == 'green':
            _col += _h
            _col += _l
        else:
            _col += _l
            _col += _h
    elif ranks['low'] == 'red':
        _col += _l
        if ranks['mid'] == 'green':
            _col += _m
            _col += _h
        else:
            _col += _h
            _col += _m
    lowers.append('<div style="background:{}"><h1>MB {}</h1></div>'.format(_col,_col))

for i, x in reversed(list(enumerate(lowers))):
    print(x)

#add base color
col='#'+str(hex(inred))[2:4]+str(hex(ingreen))[2:4]+str(hex(inblue))[2:4]

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
    _h = ''
    _m = ''
    _l = '' 
    _col = '#'
    if _high < 16: _h = '0' + str(hex(_high))[2:]
    else: _h = str(hex(_high))[2:]
    if _mid < 16: _m = '0' + str(hex(_mid))[2:]
    else: _m = str(hex(_mid))[2:]
    if _low < 16: _l = '0' + str(hex(_low))[2:]
    else: _l = str(hex(_low))[2:]
    if ranks['high'] == 'red':
        _col += _h
        if ranks['mid'] == 'green':
            _col += _m
            _col += _l
        else:
            _col += _l
            _col += _m
    elif ranks['mid'] == 'red':
        _col += _m
        if ranks['high'] == 'green':
            _col += _h
            _col += _l
        else:
            _col += _l
            _col += _h
    elif ranks['low'] == 'red':
        _col += _l
        if ranks['mid'] == 'green':
            _col += _m
            _col += _h
        else:
            _col += _h
            _col += _m

    print('<div style="background:{}"><h1>MB {}</h1></div>'.format(_col,_col))

print(end)

sys.exit()


