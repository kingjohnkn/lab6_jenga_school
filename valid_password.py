def valid_password():
    """Validate password."""
    
    print("Enter a password with more than 10 characters.")
    password = input("> ")
    
    
    while len(password) < 10:
        print("INVALID! Password has to have more than 10 characters")
        password = input("\nEnter password: ")
        
    password2 = input("Re-enter password: ")
    
    if password == password2:
        print("Perfect match! Thankyou!")
    else:
        print("ERROR! Passwords don't match!\n")
        valid_password()
        
        
valid_password()
