inventory = 0
stock_quantity = 0

while stock_quantity != "quit":
    stock_quantity = input("Enter stock quantity: ")

    if stock_quantity == "quit":
         break

    if stock_quantity.isdigit(): #Negative numbers are not digits, hence serves double error handling
        inventory += int(stock_quantity)
        print(inventory)
        if inventory > 500:
            print("Inventory has exceeded 500 units.")
            break
    else:
        print("Invalid input, please enter only integers")    

        
       
        
    
        
        
        
        
