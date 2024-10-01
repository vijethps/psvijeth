def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
x=int(input('enter a number:'))
print('factorial no is:',fact(x))

