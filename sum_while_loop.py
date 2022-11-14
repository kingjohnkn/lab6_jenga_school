def sum_of_numbers():
    """Find the sum of numbers 5 - (input from user)"""
    
    end_number = int(input("Enter the end value: "))
    
    number = 0
    i = 5
    while i <= end_number:
        number = number + i
        i += 2
        
    print(f"The sum of numbers from 5 to {end_number} is {number}")
        
sum_of_numbers()
