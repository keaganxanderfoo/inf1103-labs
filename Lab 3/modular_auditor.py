def get_valid_input():
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity == "quit":
        return stock_quantity
    elif stock_quantity.isdigit():
        return int(stock_quantity)
    else:
        print("Invalid input, please enter only positive integers")
        return False

while True:  #Create infinite loop
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        break
    