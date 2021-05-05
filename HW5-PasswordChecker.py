secret = "1941abcd"

def passwordchecker(key):
    x = 0
    while x != 5:
        key = input("Whats the password?")
        if key == secret:
            print('Access Granted')
            break
        elif key != secret:
            x = x + 1
            print("Try again")
    else:
        print("locked out")


print(passwordchecker(0))