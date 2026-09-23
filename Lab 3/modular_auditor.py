inventory = 0
stock_quantity = 0
invalid_input = 0
processed_units = 0

while stock_quantity != "quit":
    stock_quantity = input("Enter stock quantity: ")

    if stock_quantity == "quit": 
         break

    if stock_quantity.isdigit(): #Negative numbers are not digits, hence serves double error handling
        inventory += int(stock_quantity)
        processed_units += int(stock_quantity)
        if inventory > 500:
            print("Inventory has been overstocked")
            break
    else:
        print("Invalid input, please enter only integers")    
        invalid_input += 1

print("Total Processed Units:", processed_units)
print("Total Invalid Inputs:", invalid_input)
