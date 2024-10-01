def add():
    a=int(input("enter a num1:"))
    b=int(input("enter a num2:"))
    print(a+b)
def sub():
    a=int(input("enter a num1:"))
    b=int(input("enter a num2:"))
    print(a-b)
def mul():
    a=int(input("enter a num1:"))
    b=int(input("enter a num2:"))
    print(a*b)
def div():
    a=int(input("enter a num1:"))
    b=int(input("enter a num2:"))
    print(a/b)
print("enter your choice")
print("1.add(),2.sub(),3.mul(),4.div(),5.exit")
i=int(input("enter a choice number:"))

while(i<=5):
    if i==1:
        add()
    elif i==2:
        sub()
       
    elif i==3:
        mul()
       
    elif i==4:
        div()
    else:
        print("exit program")
        break
