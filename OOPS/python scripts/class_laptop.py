'''
Define all getter and setter methods + __str__()
LAPTOP
Attributes:
Brand
Processor
RAM
Color
'''
class Laptop:
    #constructor for Laptop class
    #getter and setter methods
    #__str__() method
    def __init__(self,abrand,aprocessor,aram,acolor):
        self.brand=abrand
        self.processor=aprocessor
        self.ram=aram
        self.color=acolor
    #getter and setter for instance attributes
    @property
    #getter
    def property_brand(self):
        return f'The brand is: {self.brand}' #returning the brand
    @property_brand.setter
    #setter
    def property_brand(self,value):
        self.brand=value #setting the brand
        print('Setting the brand...')
    @property
    #getter
    def property_processor(self):
        return f'The processor is: {self.processor}' #returning the processor
    @property_processor.setter
    #setter
    def property_processor(self,value):
        self.processor=value #setting the processor
        print('Setting the processor...')
    @property
    #getter
    def property_ram(self):
        return f'The ram is: {self.ram}' #returning the ram
    @property_ram.setter
    #setter
    def property_ram(self,value):
        self.ram=value #setting the ram
        print('setting the ram...')
    @property
    #getter
    def property_color(self): 
        return f'The color is: {self.color}' #returning the color
    @property_color.setter
    #setter
    def property_color(self,value):
        self.color=value #setting the color
        print('setting the color...')
    def __str__(self): #overriding str to get the details of the laptop
        return f'The details of the Laptop\nBrand : {self.brand}\nProcessor : {self.processor}\nColor : {self.color}\nRAM : {self.ram}'
if __name__=="__main__":
    ch='y' 
    while ch!='n':
        print("Enter the laptop details:")
        abrand=input("Enter the brand name:")
        aprocessor=input("Enter the processor:")
        aram=input("Enter the RAM:")
        acolor=input("Enter the color:")
        laptopObj=Laptop(abrand,aprocessor,aram,acolor) #creating the instance of the class laptop
        choice='y'
        while choice=='y':
            print("Enter 1 to set the laptop brand:")
            print("Enter 2 to set the laptop processor:")
            print("Enter 3 to set the laptop RAM:")
            print("Enter 4 to set the laptop color:")
            print("Enter 5 to see the laptop details:")
            c=input("Enter your choice:")
            if c=='1':
                laptopObj.property_brand=input("Set value to:")
                print(f'Getting the brand...\n{laptopObj.property_brand}')
            elif c=='2':
                laptopObj.property_processor=input("Set value to:")
                print(f'Getting the processor...\n{laptopObj.property_processor}')
            elif c=='3':
                laptopObj.property_ram=input("Set value to:")
                print(f'Getting the RAM...\n{laptopObj.property_ram}')
            elif c=='4':
                laptopObj.property_color=input("Set value to:")
                print(f'Getting the color...\n{laptopObj.property_color}')
            elif c=='5':
                print('-'*20,'\n',laptopObj)
            else:
                print("Wrong choice.")
            choice=input('Enter y to continue setting the value else Enter n to exit:')
        ch=input('Enter y to entry new laptop else Enter n to exit:')

            

    
    
