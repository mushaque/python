class mobile:
    # variables that are common for all instances
    mobile = '5G mobile'

    # constructor method - called when we initiate calls/instance is created
    def __init__(self,manufacturer,model):

        #Instance variables specific to each instance
        self.manufacturer = manufacturer
        self.model = model 
    
    #Instance method 
    def mobile_details(self):
        return f'5G mobile is manufactured by {self.manufacturer} and the model is {self.model} '
    
mobile1 = mobile('Apple','15 pro max')
mobile2 = mobile('Samsung','S24 ultra')
mobile3 = mobile('Redmi','Note 13 5G')
mobile4 = mobile('Iqoo','Neo 9 pro')

print(mobile1.mobile_details())