def get_valid_input():
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity == "quit":
        return stock_quantity
    elif stock_quantity.isdigit():
        return int(stock_quantity)
    else:
        print("Invalid input, please enter only positive integers")
        return False

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1

inventory = 0
invalid_input = 0
processed_units = 0

while True:  #Create infinite loop
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        break
    elif stock_quantity is False:
        invalid_input += 1

    inventory = process_delivery(stock_quantity, inventory)
    tax = calculate_tax(inventory)
print(inventory, invalid_input, tax)


        



