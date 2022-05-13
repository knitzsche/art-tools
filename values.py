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

print(head)
incol=sys.argv[1]
inred=int('0x'+incol[0:2],16)
ingreen=int('0x'+incol[2:4],16)
inblue=int(incol[4:],16)

#print('red', inred)
#print('green', ingreen)
#print('blue', inblue)

redper=inred/256
greenper=ingreen/256
blueper=inblue/256
#print('red%', redper)
#print('green%', greenper)
#print('blue%', blueper)
def get_col(col,per):
    return col*per
    #return int(hex(col),16)*per

def shades(nr,redper,ng,greenper,nb,blueper):
    run = True
    idx = -1
    while run:
        idx += 1
        nr=get_col(nr,redper)
        ng=get_col(ng,greenper)
        nb=get_col(nb,blueper)
        r = str(hex(int(nr)))[2:]
        if len(r) < 2: r = '0'+ r
        g = str(hex(int(ng)))[2:]
        if len(g) < 2: g = '0'+ g
        b = str(hex(int(nb)))[2:]
        if len(b) < 2: b = '0'+ b
        col='#' + r + g + b
        print('<div style="background:{}"><h1>MB {}</h1></div>'.format(col,col))
        if nr <= 0 or ng <= 0 or nb <= 0:
            run = False
        #if idx > 20: run = False

# strating color
col='#'+incol
print('<div style="background:{}"><h1>MB {}</h1></div>'.format(col,col))

nr=inred
ng=ingreen
nb=inblue

shades(nr,redper,ng,greenper,nb,blueper)

print(end)
