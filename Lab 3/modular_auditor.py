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
    return round(amount * 0.1)

def generate_report(total_units, failed_attempts):
    print("Total Processed Units:", total_units)
    print("Total Invalid Inputs:", failed_attempts)

inventory = 0
invalid_input = 0
deliveries = 0
total_tax = 0

while True:  #Create infinite loop
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        break
    elif stock_quantity is False:
        invalid_input += 1

    inventory = process_delivery(stock_quantity, inventory)
    deliveries += 1 #Track number of deliveries (E.g No. of Batches)

    if inventory > 500:
        print("Inventory has been overstocked")
        break

    tax = calculate_tax(stock_quantity)
    print("Tax for this batch: ", tax)
    total_tax += tax


generate_report(inventory, invalid_input)
print(total_tax)


        



