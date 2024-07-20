mst_pwd=input("what is the master password?")
def view():
    f=open("password.txt","r")
    for line in f.readlines():
        data=line.rstrip()
        name,pwd=data.split("|")
        print("user:",name, "password:",pwd)
    f.close()
def create():
    name=input("account name: ")
    pwd=input("password: ")
    f1=open("password.txt","a")
    f1.write(name + "|" + pwd + "\n")
    f1.close()
while True:
    user_input=input("do you want to create a new password or view a password? or press Q to quit ")
    if( user_input=="view"):
        view()
    elif (user_input=="create"):
        create()
    elif (user_input.lower()=="q"):
        break
    else:
        print("invalid input!")
        continue
print('over')