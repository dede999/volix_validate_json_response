PRODUCTS_TO_CHECK = 20

def setup_verification(argumets):
    if len(argumets) < 1:
        print("Usage: python3 main.py <file_name> <products_count (default = 20)>")
        return
    
    file_name = argumets[0]
    products_count = argumets[1] if len(argumets) == 2 else PRODUCTS_TO_CHECK
    
    return file_name, products_count
