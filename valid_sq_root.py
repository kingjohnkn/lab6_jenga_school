def valid_squareroot():
    """Validates a number has a valid square root."""
    
    x = int(input("Enter the number for the Square Root: "))
    
    while x < 0:
        print("Number cannot be negative ...")
        x = int(input("Enter the number for the Square Root: "))
        
    print("The square root of", x, "is", x**0.5)
    
valid_squareroot()