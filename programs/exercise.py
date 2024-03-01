# it is a sequence of characters that forms a search pattern.
# re module offers a set of functions that allows us to search a string for a match:
import re

def validate_phone(phone):
    # Phone number pattern: ###-###-####
    # #  r'^\d{10}$' :##########
    # pattern = r'^\d{10}$'
    # pattern = r'^\d{+91}$'
    #  pattern = r"^[6-9]\d{9}$" 
    #  pattern = r'^\d{3}-\d{3}-\d{4}$' 
    #  pattern =r"^((0091)|(\+91)|0?)[6-9]\d{9}$"
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"

    # pattern = r'^\d{10}$'
    # Starts with 3 digits*
   # Followed by a dash,# Followed by 4 digits,# Followed by 0 or more characters that aren't newlines**
   # Followed by the end of the string.
    return re.match(pattern, phone) is not None
    # A return statement is used to end the execution of the function call

def validate_password(password):
    # Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

def main():
    # Getting user input for phone number and password
    phone = input("Enter your phone number:")
    password = input("Enter your password: ")

    # Validating phone number and password
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Invalid phone number format. Please enter in the format ###-###-####.")

    if validate_password(password):
        print("Password is valid.")
    else:
        print("Invalid password. Password must contain at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, and be at least 8 characters long.")

main()

























# import re

# def validate_phone(phone):
#     # Phone number pattern: ###-###-####
#     #  r'^\d{10}$'
#     pattern = r'^\d{3}-\d{3}-\d{4}$' 
# # Starts with 3 digits*
# # Followed by a dash
# # Followed by 4 digits
# # Followed by 0 or more characters that aren't newlines**
# # Followed by the end of the string.
#     return re.match(pattern, phone) is not None

# def validate_password(password):
#     # Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
#     if len(password) < 8:
#         return False
    
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_symbol = False
    
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         else:
#             has_symbol = True
    
#     return has_upper and has_lower and has_digit and has_symbol

# def main():
#     # Getting user input for phone number and password
#     phone = input("Enter your phone number (in the format ###-###-####): ")
#     password = input("Enter your password: ")

#     # Validating phone number and password
#     if validate_phone(phone):
#         print("Phone number is valid.")
#     else:
#         print("Invalid phone number format. Please enter in the format ###-###-####.")

#     if validate_password(password):
#         print("Password is valid.")
#     else:
#         print("Invalid password. Password must contain at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, and be at least 8 characters long.")

#
#     main()
