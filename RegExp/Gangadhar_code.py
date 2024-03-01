# define a function for calculating
# the area of a shapes
def checking_string_to_float(float_vlaue):
    try:
        float_converted = float(float_vlaue)
        return True
    except ValueError:
        return False



def calculate_rectangle_area():

    # converting all characters into lower cases
    
    l = input("Enter rectangle's length in meters: ")
    if checking_string_to_float(l):
        l = float(l)
        b = input("Enter rectangle's breadth in meters: ")
        if checking_string_to_float(b):
            b = float(b)
        else:
            print(f'value{b} cannot be considered as number  or decimal')
        
        if l >=0  and b >=0:
            a = l*b
            text = f'Area of rectangle with length: {l}, breadth: {b} is {a}'
            print(text)

    else:
        print(f'value{l} cannot be considered as number  or decimal')
        

def check_shape(shape):
    
    shape = shape.lower()
    shapes = ['rectangle']

    if shape in shapes:
        if shape == 'rectangle':
            calculate_rectangle_area()
    else:
        print(f'sorry!, we are not supporting {shape} as of now')

        
            
    
    


check_shape('rectanglee')
