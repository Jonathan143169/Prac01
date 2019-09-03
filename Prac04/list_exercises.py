def main():
    numbers = []
    for number in range(1, 6):
        user_input = int(input("Number: "))
        numbers.append(user_input)
    average = sum(numbers)/len(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The lst number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input("Please enter your username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
