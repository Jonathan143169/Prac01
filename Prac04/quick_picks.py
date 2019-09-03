import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():

    random_picks = int(input("How many quick picks? "))
    for picks in range(1, random_picks + 1):
        number_list = []
        for number in range(NUMBERS_PER_LINE):
            selected_number = random.randint(MINIMUM, MAXIMUM)
            while selected_number in number_list:
                selected_number = random.randint(MINIMUM, MAXIMUM)
            number_list.append(selected_number)
        number_list.sort()

        print(" ".join("{:2}".format(selected_number) for selected_number in number_list))


main()
