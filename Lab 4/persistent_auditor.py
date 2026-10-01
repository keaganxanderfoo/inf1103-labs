def load_orders(filename="orders.txt"):
    orders = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                order_id, name, qty = int(parts[0]), parts[1], int(parts[2])
                orders.append([order_id, name, qty])
    except FileNotFoundError:
        orders = []
    return orders


def display_orders(orders):
    print("Current Orders:\n")
    for order_id, name, qty in orders:
        print(f"{order_id}, {name}, {qty}")
    print()

def get_valid_quantity():
    while True:
        quantity = input("Enter Quantity: ")
        if quantity.isdigit():
            return int(quantity)
        else:
            print("Invalid input, please enter only positive integers")


def get_next_order_id(orders):
    if not orders:
        return 1001
    return max(order[0] for order in orders) + 1


def main():
    orders = load_orders()
    display_orders(orders)

    while True:
        product_name = input("Enter Product Name: ")
        if product_name.lower() == "quit":
            break

        quantity = get_valid_quantity()
        new_id = get_next_order_id(orders)
        orders.append([new_id, product_name, quantity])

        print()
        print("New Order Added:")
        print(f"{new_id},{product_name},{quantity}")
        print()


if __name__ == "__main__":
    main()