"""
1. When will a ValueError occur?
If the numerator and denominator contains a character

2. When will a ZeroDivisionError occur?
When the denominator is zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""



def main():
    numerator = int(input("Enter the numerator: "))
    while denominator == 0:
        try:
            denominator = int(input("Enter the denominator: "))
            fraction = numerator / denominator
            print(fraction)
        except ValueError:
            print("Numerator and denominator must be valid numbers!")
        except ZeroDivisionError:
            print("Cannot divide by zero! Enter valid denominator")
    print("Finished.")


main()
