items = 1
total_price = 0
price = 0
discount = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for items in range(number_of_items):
    price = float(input("Price of item: $"))
    total_price = total_price + price

if total_price > 100:
    discount = (10 / 100) * total_price
    total_price = total_price - discount

print("The price of {}  is  {:.2f}$".format(number_of_items, total_price))
