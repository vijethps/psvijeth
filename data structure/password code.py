l=0
u=0
s=0
aln=0
p=input("enter the pass word:")
if(len(p)>=8):
    for i in p:
        if(i.islower()):
            l=l+1
        elif(i.isupper()):
            u=u+1
        elif(i.isalnum()):
            aln=aln+1
        elif(i=='@',i=='#'):
             s=s+1
    if(l>=1 and s>=1 and u>=1 and aln>=1):
        print("valid")
    else:
        print("not valid")
else:
    print("not valid")
