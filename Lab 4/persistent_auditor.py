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


def main():
    orders = load_orders()
    display_orders(orders)


if __name__ == "__main__":
    main()