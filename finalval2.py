def finalval2():
    """Value of x."""
    
    x = 7
    while x >= 5 and x <= 8:
        print(x)
        if x%2 == 0:
            x = x + 1
        else:
            x = x - 2
    
    print("Final Value:", x)
    
finalval2()