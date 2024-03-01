"""
create a code to validate user form with fields,phone and password 
and phone number should be in format 
and password must be alpha numeric,contains atleat one caps,small,number,symbol and there should be min char length
"""
# import re --->The re module in python allows us to perform regex matching operations.
import re
def validate_phone(phone):
    
    # phone_regex1=r'\d\d\d\d-\d\d\d\d'
    # return re.match(phone_regex1, phone) 

    # phone_regex2=r"^[789]\d{9}$" 
    # return re.match(phone_regex2, phone) 

    # phone_regex3=r"^\d{3}-\d{3}-\d{4}$"
    # return re.match(phone_regex3, phone) 

    # phone_regex4=r"^\d{10}$"
    # return re.match(phone_regex4, phone) 

    # phone_regex5=r"^\+91\s?\d{5}-\d{5}$"
    # return re.match(phone_regex5, phone) 

    # phone_regex6=r"^\+44\s?\d{2,5}\s?\d{4}\s?\d{4}$"
    # return re.match(phone_regex6, phone) 

    phone_regex7=r'\d{3}[-.]?\d{3}[-.]?\d{4}'
    return re.match(phone_regex7, phone) 

    # phone_regex8=r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
    # return re.match(phone_regex8, phone) 

def validate_password(password):
    # Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
    pwd_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pwd_regex, password)


def main():
    # Getting user input for phone number and password
    phone = input("Enter your phone number:")
    password = input("Enter your password: ")
   

    # Validating phone number and password
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Invalid phone number format. Please enter in the format")
    if validate_password(password):
        print("Password is valid.")
    else:
        print("Invalid password. Password must contain at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, and be at least 8 characters long.")
main()



