def get_valid_input():
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity == "quit":
        return stock_quantity
    elif stock_quantity.isdigit(): #Only if stock quantity is a positive integer, then value is returned
        return int(stock_quantity)
    else:
        print("Invalid input, please enter only positive integers")
        return False

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return round((amount * 0.1),2)

def generate_report(total_units, failed_attempts):
    print("Total Processed Units:", total_units)
    print("Total Invalid Inputs:", failed_attempts)

def load_inventory(filename="inventory.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            inventory = 0
            history = []
            run_count = 0
            for line in lines:
                line = line.strip()
                if line.startswith("Run"):
                    run_count += 1
                elif line.startswith("Total Processed: "):
                    inventory = int(line.split(":")[1].strip())
                elif line.startswith("Total Entries:"):
                    entries_str = line.split(":")[1].strip()
                    if entries_str:
                        history = [int(x) for x in entries_str.split(",")]
            return inventory, history, run_count
    except FileNotFoundError:
        return 0, [], 0

def save_inventory(inventory, history, run_number, filename="inventory.txt"):
    with open(filename, "a") as f:
        f.write(f"\nRun {run_number}:\n")
        f.write(f"Total Processed: {inventory}\n")
        f.write(f"Total Entries: {','.join(str(x) for x in history)}\n")
    print(f"Order successfully saved to {filename}")

inventory, history, run_count = load_inventory()
current_run = run_count + 1
invalid_input = 0
deliveries = 0
total_tax = 0

while True:  #Create infinite loop
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        save_inventory(inventory, history, current_run)
        break
    elif stock_quantity is False:
        invalid_input += 1
        continue


    inventory = process_delivery(inventory, stock_quantity)
    history.append(stock_quantity)
    deliveries += 1 #Tracks number of deliveries (E.g No. of Batches)

    tax = calculate_tax(stock_quantity)
    print("Tax for this delivery: ", tax)
    total_tax += tax #Tracks the total amount taxed across all delivery batches

    if inventory > 500: 
        print("Inventory has been overstocked")
        save_inventory(inventory, history, current_run)
        break

generate_report(inventory, invalid_input)

        



