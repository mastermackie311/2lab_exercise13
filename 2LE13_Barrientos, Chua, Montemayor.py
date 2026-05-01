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
