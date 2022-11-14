def sum_of_numbers():
    """Find the sum of numbers 5 - (input from user)"""
    
    end_number = int(input("Enter the end value: "))
    end_number = end_number + 1

    number = 0
    for i in range(5, end_number, 2):
        number = number + i
        
    print(f"The sum of numbers from 5 to {end_number - 1} is {number}")
    
sum_of_numbers()
