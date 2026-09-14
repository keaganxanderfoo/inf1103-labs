inventory = 0
stock_quantity = 0

while stock_quantity != "quit":
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity.isdigit():
        inventory += int(stock_quantity)
        print(inventory)
        
    
        
        
        
        
