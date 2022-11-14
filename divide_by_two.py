def divide_by_two():
    """Divide a number by two"""
    
    x = 1.0
    counter = 0
    
    while x > 0:
        # There is no difference to using x > 0 or x != 0
        x = x / 2
        print(x)
        counter += 1
    
    print(f"\nx reaches {counter} steps to get to 0.")
    
divide_by_two()