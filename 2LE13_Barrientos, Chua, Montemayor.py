while True:
    
    try:
        file = open("shopee.txt", "x")
        print("File created successfully")
        file.close()
    except FileExistsError:
        print("File already exists")
    except FileNotFoundError:
        print("File not found")