n=int(input("enter a num:"))
count=0
for i in range(2,n):
    if (n%i==0):
        count=count+1
if(count==0):
    print("not composite")
else:
    print("composite")
