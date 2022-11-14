def item_price():
    """Calculate the price of items to a certain budget."""
    
    budget = 0
    while budget <= 100:
        price = int(input("How much is the item? "))
        budget1 = budget
        budget = budget + price
        if budget > 100:
            print(f"Your budget will exceed 100TL. You're at {budget1}TL")
        else:
            print(f"You're at {budget}TL")

item_price()