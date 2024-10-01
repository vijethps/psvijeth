mail=input('enter amail id:')
if('@'in mail and mail.count('@')==1):
    if(mail.endswith('gmail.in') or mail.endswith('gmail.com')):
        if(mail.islower()):
            print('mail id is valid')
        else:
            print('not valid')
    else:
        print("not valid")
else:
    print("not valid")
