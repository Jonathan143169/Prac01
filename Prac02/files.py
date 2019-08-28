in_file = open("name.txt", "w")
name = input("Enter your name: ")
print("Your name is {}".format(name), file=in_file)
in_file.close()

in_file = open("name.txt", "r")
print("Name: ", in_file.read().strip() + '.')
in_file.close()

num_file = open("numbers.txt", "r")
first_number = int(num_file.readline())
second_number = int(num_file.readline())
# print(first_number + second_number)
num_file.close()

out_file = open("numbers.txt", "r")
result = 0
for line in out_file:
    numbers = int(line)
    result = result + numbers
out_file.close()
print(result)
