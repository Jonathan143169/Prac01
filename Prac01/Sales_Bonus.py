
amount = 1000
sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if amount > sales > 0:
        print(sales * 0.1)
    elif sales >= amount and sales > 0:
        print(sales * 0.15)

