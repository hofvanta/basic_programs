import sys
from getpass import getpass


def ask_username():
    username = input("Geef usernaam: ")
    username = username.strip()
    userlen = len(username)
    if userlen < 3:
        print("Username to short")
        sys.exit(1)
    if '\t' in username:
        print("Username bevat een tap!")
        sys.exit(42)
    elif ' ' in username:
        print("Username bevat een spatie")
        sys.exit(42)
    return username


def ask_password(username):
    password = getpass("Geef password: ")
    if len(password) < 5:
        print("Password to short!")
        sys.exit(46)
    if password == username:
        print("Password en username mogen niet gelijk zijn!")
        sys.exit(45)
    return password


def is_welcome(name, passwd):
    '''implement'''
    return False  # fixture, replace


def main():
    username = ask_username()
    password = ask_password(username)

    if is_welcome(username, password):
        message = "Welcome in " + username + "."
    else:
        message = "Not allowed."
        print(message)
    sys.exit(0)


if __name__ == "__main__":
    main()