def sell_product(inventory, product_name, quantity):
    if product_name in inventory:
        if inventory[product_name]["stock"] >= quantity:
            inventory[product_name]["stock"] -= quantity
            print(f"Sold {quantity} of {product_name}.")
        else:
            print(f"Error: Insufficient stock for {product_name}.")
    else:
        print(f"Error: {product_name} not found in inventory.")

def calculate_total_value(inventory):
    total_value = 0
    for product in inventory.values():
        total_value += product["price"] * product["stock"]
    return total_value

def identify_low_stock(inventory, threshold=10):
    low_stock_items = [name for name, info in inventory.items() if info["stock"] < threshold]
    return low_stock_items

if __name__ == "__main__":
    inventory = {
        "Laptop": {"price": 60000, "stock": 5},
        "Mouse": {"price": 500, "stock": 50},
        "Keyboard": {"price": 1500, "stock": 20}
    }

    print("Initial Inventory Value:", calculate_total_value(inventory))
    
    sell_product(inventory, "Laptop", 2)
    sell_product(inventory, "Laptop", 10) 
    
    print("New Inventory Value:", calculate_total_value(inventory))
    print("Low Stock Items:", identify_low_stock(inventory))
