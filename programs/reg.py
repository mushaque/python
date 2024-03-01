"""
create a code to validate user form with fields,phone and password 
and phone number should be in format 
and password must be alpha numeric,contains atleat one caps,small,number,symbol and there should be min char length
"""
# PROGRAM:

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


# Explanation:

"""
import re --->The re module in python allows us to perform regex matching operations

Symbol 				Matches
+ 			One or More of the preceding group
*		 	Zero or More of preceding group
? 			Zero or One of preceding group
^			name String must begin with the name/Matches the start of the string.
name$ 			String must end with the name
. 			Any character except \n
{n} 			Exactly n of preceding group
{n, } 			>= n of preceding group
{,n} 			[0, m] of preceding group
{n, m} 			[n, m] of preceding group
*? 			Non Greedy matching of the preceding group
[abc] 			Any character enclosed in the brackets
[^abc] 			Any character not enclosed in the brackets
\d, \w, \s 		Digit, word, or space respectively.
\D, \W, \S 		Anything except digit, word, or space respectively
\s? 			0 or 1 whitespace.
(\d*) 			0 or more digit characters.
(.+) 			Greater than or equal to 1 characters.
\s			Single Whitespace
([A-Z]{2, 3})		2 or 3 Uppercase alphabets
(\d{4})			4 digit characters
[6-9] 			Matches any digit from 6 to 9 (valid starting digits for Indian mobile numbers).
\d{9} 			Matches exactly 9 digits (totaling 10 digits including the starting digit).
\d			Matches any digit from 0-9.
$ 			Matches the end of the string.
\s			Matches any whitespace character.
\			Indicates that the next character is a literal rather than a special character.
(\d{1,2})		captures upto two digits(ie; one or two digits).


--->1.Landline number
Regular expression:r'\d\d\d\d-\d\d\d\d'
This pattern tells after 4 digits  consist of '-' and we have type other 4 digits
Examples of valid numbers:
2435-4153

--->2.Indian Mobile Numbers (10 digits, starting with 9, 8, or 7):
This pattern matches Indian mobile numbers that consist of 10 digits and start with 9, 8, or 7.
Regular expression: r"^[789]\d{9}$" / pattern = r"^[6-9]\d{9}$"
Examples of valid numbers:
9882223456
8976785768
7986576783

--->3.US Telephone Numbers (XXX-XXX-XXXX format):
This pattern matches US telephone numbers in the format XXX-XXX-XXXX (where X represents a digit).
Regular expression:r"^\d{3}-\d{3}-\d{4}$"
Examples of valid numbers:
123-456-7890
987-654-3210

--->4.Strictly Digits (10 digits only):
Regular expression:r"^\d{10}$"
Example: 1234567890

--->5.Indian Format (with or without country code):
Regular expression: r"^\+91\s?\d{5}-\d{5}$"
Example: +91 12345-67890 or 01234-567890

--->6.UK Format (with or without spaces):
Regular expression: r"^\+44\s?\d{2,5}\s?\d{4}\s?\d{4}$"
Example: +44 20 1234 5678

--->7.we want to match phone numbers in the format of “123-456-7890” or “123.456.7890”.
Regular expression:r'\d{3}[-.]?\d{3}[-.]?\d{4}'
Examples of valid numbers:
123-456-7890
987.654.3210

--->8.General Phone Numbers (with optional country code and separators):
This pattern allows for variations in country codes (optional), separators (such as spaces, hyphens, or dots), and different digit groupings.
Regular expression: r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
Examples of valid numbers:
+91-9883443344
0091-9883443344
919883443344
09883443344


Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
Regular expression:r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

The regex pattern r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$' checks the following conditions:
1.At least 8 characters long.
2.Contains at least one uppercase letter ([A-Z]).
3.Contains at least one lowercase letter ([a-z]).
4.Contains at least one digit (\d).
5.Contains at least one special character from @#$%^&+=.
"""