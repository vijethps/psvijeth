x=input("enter the content of decode:")
y=" "
for i in range(0,len(x),2):
    z=chr(int(x[i:i+2]))
    y=y+z
print(y)
