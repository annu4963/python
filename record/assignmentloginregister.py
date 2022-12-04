def register():
    ans=input("Do you have username and password")
    if ans=='yes':
        print("Welcome to Login page")
    else:
        name=input("Enter your name")
        pass=input("Enter your password")
        conf=input("Enter confirm password")
            obj=open('usernamepassword.txt','w')
            obj.write(name)

def login():
    username=input("Enter username")
    password=input("Enter password")
    obj = open('usernamepassword.txt', 'r')
    print(obj.read())