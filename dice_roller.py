import random
print("roll the dice!!")
while True:
    user_input=input("roll:")
    if user_input.lower()=="0":
        random_no=random.randint(1,6)
        print(random_no)
        while random_no==6:
            print("roll the dice again!")
            rand2=random.randint(1,6)
            print(rand2)
            break
    else:
        print("you quit the game")
        quit()
print("done!")


