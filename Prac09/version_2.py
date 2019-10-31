import os


def main():
    extension = {}
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue
        file_extension = file.split('.')[-1]
        if file_extension not in extension:
            user_input = input("What category would you like to sort {} files into".format(file_extension))
            extension[file_extension] = user_input
            print(extension)
            try:
                os.mkdir(user_input)
            except FileExistsError:
                pass

        os.rename(file, "{}/{}".format(extension[file_extension], file))


main()
