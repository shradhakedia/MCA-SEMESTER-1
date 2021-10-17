'''1. Create a class Computer having attributes Color, Brand, Processor, RAM. 
Define functions to initialize these and fetch these attributes.
#constructor
#Accessor (getter)
#Mutators (setter)
#Class var: count no of object
#class set : display count
#compare 
 
  
'''
class Computer:
    count=0
    def __init__(self,acolor,abrand,aprocessor,aRAM):
        self.color=acolor 
        self.brand=abrand
        self.processor=aprocessor
        self.RAM=aRAM
        Computer.count+=1
    def set_color(self):
        self.color="Space Grey"
    def get_color(self):
        return f"the color is {self.color}"
    def get_brand(self):
        return f"the brand is {self.brand}"
    def get_processor(self):
        return f"the processor is {self.processor}"
    def get_ram(self):
        return f"the RAM is {self.RAM}"
    def compare(self,color,brand,processor,ram):
        if self.color==color and self.brand==brand and self.processor==processor and self.RAM==ram:
            print("All the attributes of Objects are same.")
        else:
            print("All the attributes of Objects are not same.")
    @classmethod
    def display_count(cls):
        return cls.count
if __name__=="__main__":
    obj1=Computer(input("Enter the color for object1:"),input("Enter the brand for object1:"),input("Enter the processor for object1:"),input("Enter the RAM for object1:"))
    obj2=Computer(input("Enter the color for object2:"),input("Enter the brand for object2:"),input("Enter the processor for object2:"),input("Enter the RAM for object2:"))
    print("The no. of object created is:",obj1.display_count())
    print(f"{obj1.get_color()} \n{obj1.get_brand()} \n{obj1.get_processor()} \n{obj1.get_ram()}")
    obj1.compare(obj2.color,obj2.brand,obj2.processor,obj2.RAM)
    obj1.set_color()
    print("After changing object1 color:",obj1.get_color())
