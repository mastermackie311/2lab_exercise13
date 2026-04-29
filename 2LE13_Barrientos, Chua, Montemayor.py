while True:
    
    try:
        file = open("shopee.txt", "x")
        print("File created successfully")
        file.close()
    except FileExistsError:
        print("File already exists")
    except FileNotFoundError:
        print("File not found")

    def addItem():
        with open("shopee.txt", "a") as file:
            itemName = input("Item name: ")
            itemQuantity = int(input("Item quantity: "))
            itemPrice = float(input("Item price: "))
            file.write(f"Item: {itemName}, Quantity: {itemQuantity}, Price: {itemPrice}\n")
            print("\n", itemName, "has been added to your cart.")
    
    def viewCart():
        with open("shopee.txt", "r") as file:
            content = file.read()
            print("\n--- Shopping Cart ---")
            print(content)

    def removeItem():
        with open("shopee.txt", "r") as file:
            itemRemove = input("Enter the name of the item to remove: ")
            lines = file.readlines()
            found = False
            with open("shopee.txt", "w") as file:
                for line in lines:
                    if itemRemove in line:
                        found = True
                    else:
                        file.write(line)
    
    def itemCheckout():
        with open("shopee.txt", "r") as file:
            content = file.read()
            print("\n--= Checkout =--")
            totalPrice = 0
            for line in content.splitlines():
                if "Price: " in line and "Quantity: " in line:
                    price = float(line.split("Price: ")[1])
                    totalPrice += price
            print(content)
            print(f"Total price: {totalPrice}")
            print("Thank you for shopping with us!")
            open("shopee.txt", "w").close()  # Clear the cart after checkout
    
    def main():

        print("\nMenu:", "\n1. Add items", "\n2. Remove items", "\n3. View cart", "\n4. Checkout")

    while True:

        userOperation = input("\nChoose operation: ")

        if userOperation == "1":
            addItem()
        elif userOperation == "2":
            removeItem()
        elif userOperation == "3":
            viewCart()
        elif userOperation == "4":
            itemCheckout()
        else:
            print("Operation not found. Try again.")
            print("\nMenu:", "\n1. Add items", "\n2. Remove items", "\n3. View cart", "\n4. Checkout")
            continue

main()