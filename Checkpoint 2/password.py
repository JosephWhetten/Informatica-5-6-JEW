import getpass

def main():
    
    password = getpass.getpass("Set a password: ")
    input("Press enter to continue ")
    check_password(password)
    print("The program has ended.")
    
def check_password(p):
    i = 1
    xpassword = input("Enter password again to verify: ")
    if p == xpassword:
        print("The password is correct")
    else:
        while i < 3:
            i = i + 1
            xpassword = input("The password is incorrect, try again: ")
            if p == xpassword:
                print("The password is correct")
                i = 3

main()