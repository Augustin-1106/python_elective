stock = {
    'item1': 10,
    'item2': 5,
    'item3': 3
}

price = {
    'item1': 10,
    'item2': 5,
    'item3': 3
}

def display_stock():
    print("Available items in stock:")
    for item in stock:
        print(f"{item}: {stock[item]}")

def calculate_bill(items, number):
    total_bill = 0
    i=0
    for item in items:
        if item in stock and stock[item] > 0:
            total_bill += number[i]*price[item]
            stock[item] -= number[i]
            i+=1
    return total_bill

def display_remaining_stock():
    print("Remaining items in stock:")
    for item in stock:
        print(f"{item}: {stock[item]}")

display_stock()
no_items1 = []
while True:
    items_to_buy = input("Enter the items you want to buy (separated by commas): ").split(",")

    no_items = input("Enter the no of items you want to buy (separated by commas): ").split(",")
    for i in no_items:
        no_items1.append(int(i))

    total_bill = calculate_bill(items_to_buy, no_items1)
    print(f"Total bill: ${total_bill}")

    display_remaining_stock()