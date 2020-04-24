info = {}
def newusers():
    name = input("Please enter your name:")
    if name in info:
        name = input("The name is used, please enter a different one:")
    else:
        password = input("Set your password:")
        info.update({name:password})
        print("Welcome", name)

def oldusers():
    name = input("Please enter your username:")
    password = input("Please enter your password:")
    if info.get(name) == password:
        print(name, 'Welcome back ')
    else:
        print('Login incorrect')

def exit():
    return

def login():
    option = '''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
                    '''
    print(option)
    switch = {'N': newusers, 'O': oldusers, 'E': exit}
    choice = input("Enter your choice:")
    switch[choice]()

if __name__ == '__main__':
    login()