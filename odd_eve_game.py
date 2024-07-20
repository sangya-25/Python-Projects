import random
print("welcome to this game!!")
user_wins=0
comp_wins=0
user_ch=input("enter odd or eve: ")
if (user_ch=="eve"):
    comp_ch="odd"
    print(comp_ch)
elif (user_ch=="odd"):
    comp_ch="eve"
    print(comp_ch)
else:
    print("invalid input!")
user=int(input("enter your number: "))
comp=random.randint(1,10)
print(comp)
if (user+comp)%2==0:
    if(user_ch=="eve"):
        print("user wins the round")
        choice=input("choose batting or balling? :")
    else:
        print("comp wins the round!")
        ch=["batting","balling"]
        c=random.randint(0,1)
        computer_choice=ch[c]
        print(computer_choice)
else:
    if(user_ch=="odd"):
        print("user wins the round!")
        choice=input("choose batting or balling? :")
    else:
        print("comp wins the round!")
        ch=["batting","balling"]
        c=random.randint(0,1)
        computer_choice=ch[c]
        print(computer_choice)
usernotOut = 'true'
userruns = 0
compnotOut = 'true'
compruns = 0
if(user == "batting"):
    while(usernotOut):
        urun = int(input("Enter your score from 1-6: "))
        crun = random.randint(1,6)
        if(urun == crun):
            print("Comp choosed", crun)
            print("Uffo You're Out !😥")
            print("You scored ! ", userruns, " runs")
            notOut = 'false'
            break
            
        else:
            print("Comp choosed", crun)
            userruns+=urun
            print('current score is: ', userruns)

else:
    while(compnotOut):
        urun1 = int(input("Enter your score from 1-6: "))
        crun1 = random.randint(1,6)
        if(urun1 == crun1):
            print("Comp choosed", crun1)
            print("Yeah computer is out !☺️")
            print("computer scored ! ", compruns, " runs")
            notOut = 'false'
            break
            
        else:
            print("Comp choosed", crun1)
            compruns+=crun1
            print('current score is: ', compruns)

            

print('Thanks for Playing! ')











