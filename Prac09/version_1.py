import os


def main():
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            pass
        file_extension = file.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        # print("{}/{}".format(file_extension, file))
        # os.rename(file, "{}/{}".format(file_extension, file))


main()
