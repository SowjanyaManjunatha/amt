AMT=10000
print("welcome to Canara Bank")
print("insert the card")
print("please wait")
print("do not remove chip card")
print("your transaction is being processed")
print("please select the language")
print("1-hindi")
print("2-telugu")
print("3-kannada")
language=int(input())
if(language==1):
    print("you can proceed with the english language")
elif(language==2):
    print("you can proceed with the telugu language")
elif(language==3):
    print("you can proceed with the kannada language")
else:
    print("invalid choice,try again later")

print("please enter your pin number")
pin=int(input())
if(pin==7337):
    print("select your services")
    print("1-withdrawal")
    print("2-balance enquiry")
    print("3-pin change")
elif(pin==1234):
    print("incorrect password")
else:
    print("invalid password,try again later")

services=int(input())
if(services==1):
    print("please select your account type")
    print("1-savings")
    print("2-current")
    print("3-credit") 
elif(services==2):
    print("please select your account type")
    print("1-savings")
    print("2-current")
    print("3-credit")
    account_type = int(input())
    if account_type == 1:
        print("please wait your transaction is being processed")
        print("available balance:",AMT)
    elif account_type == 2:
        print("please wait your transaction is being processed")
        print("available balance:",AMT)
    elif account_type == 3:
       print("please wait your transaction is being processed")
       print("available balance:",AMT)
    else:
        print("invalid choice,try again later")
elif(services==3):
    print("select green pin/forget pin")
    print("enables you to set your own pin")
    print("1-generate otp")
    print("2-cancel")
    pin_change_choice = int(input("enter your choice 1/2"))
    if pin_change_choice == 1:
        print("please enter last your digit of your bank account")
        last_digit= int(input())
        if last_digit == 9632 :
            print("please enter the otp recevied on your register phone number")
        elif last_digit :
            print("please correct account number")
        else:
            print("invalid,try again later")

        otp = int(input())
        if otp == 9573 :
            print("otp verifed successfully")
            new_pin = int(input("enter new pin"))
            new_pin
            confirm_pin = int(input("confirm pin"))
            confirm_pin
            print("pin changed successfully")
            print("please remove your card")
            print('thank you,visit again')
        elif otp == 1234 :
            print("incorrect otp")
        else:
            print("invalid otp")
        
    elif pin_change_choice == 2:
        print("pin change cancelled")

account=int(input())
account=int(input("enter the amount:"))
print("please wait your transaction is being processed")
print("-------------------------------")
print("please collect your cash")
print("-------------------------------")
print("do you want to collect the recipt")
print("1-yes")
print("2-no")
receipt=int(input())
if receipt==1:
    print("------------------------")
    print("your available balance=",AMT-account)
    print("thank you,visit again")
elif receipt==2:
    print("thank you,visit again") 
    print("thank you,please remove your card")
else:
    print("please remove your card,thank you")  




