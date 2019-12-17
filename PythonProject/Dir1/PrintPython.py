s = "python for life"
a = s.split(" ")
for i in range(0,3):
    print(a[i])
print('=============')

print(s[2:6], end= " ")
print(s[7:10])
print(s[8:10], end= " ")
print(s[11:13])

print('=============')
print(s.upper())

print('=============')
print(s[0:6].upper(),s[7:10],s[11:15].upper() )

print('=============')
print(s[0:6],s[7:10],s[11:15].upper() )