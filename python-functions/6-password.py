def validate_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check uppercase, lowercase, and digits
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
            
    if not has_uppercase or not has_lowercase or not has_digit:
        return False
        
    # Check for spaces
    if " " in password:
        return False
    
    return True
