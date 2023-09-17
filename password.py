s='123sfhhl'
if len(s)<4:
    print('INVALID')
if s[0].isdigit():
    print('INVALID')
d=0
c=0
l=0
for i in s:
    if i.isdigit():
        d=1
    if i==" " or i=='/':
        l=1
        break 
    if ord(i)>=64 and ord(i)<=90:
        c=1
if l==1:
    print('Invalid')
elif d==1 and c==1:
    print('Valid')
else:
    print('INVALID')



