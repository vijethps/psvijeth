name=""
accountnum=0
branchcode=0
mobile=0
bal=0
amount=0
def createaccount():
    name=input("enter name:")
    accountnum=int(input("enter account num:"))
    branchcode=int(input("enter branch cude:"))
    mobile=int(input("enter mobile num:"))
def deposite(amount):
    bal=bal+amount
    checkbalance()
def withdraw(amount):
    bal=bal-amount
    checkbalance()
def checkbalance():
    print("balance:",bal)
print("1.create account,2.deposite,3.withdraw,4.checkbalance")
a=int(input("enter a choice:"))

if(a==1):
    createaccount()
elif(a==2):
    amount=int(input("enter a deposite amont:"))
    deposite(amount)
elif(a==3):
    amount=int(input("enter a with draw amount:"))
    withdraw(amount)
               
elif(a==4):
    checkbalance()
else:
    print("enter option below 4")
