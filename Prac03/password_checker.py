MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():

    password = get_password()
    print("{}".format(len(password) * '*'))
def get_password():
    password = input("> ")
    while not(password):
        print("Invalid password!")
        password = (input("> "))
    return password


main()
