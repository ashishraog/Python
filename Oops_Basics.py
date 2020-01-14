#Basic Class structure
class MyClass:   
        # assign the values to the MyClass attributes 
        number = 0       
        name = "noname"
  
def Main():   
        me = MyClass()   # Here, 'me' is the object 
        me.number = 1337     # Accessing the attributes of MyClass 
        me.name = "Harssh"   # using the dot(.) operator 
        print("%s %s" %(me.name,me.number))
        print(me.name,(me.number),sep=" ")# str is an build-in function # creates an string #ERROR      
# telling python that there is main in the program. 
if __name__=='__main__':   
        Main()


#Method
#class Vector2D: 
#        x = 0.0
#        y = 0.0
#        def Set(self, x, y=2):    # Creating a method named Set   
#                self.x = x 
#                self.y = y 
#  
#def Main(): 
#        vec = Vector2D()      # vec is an object of class Vector2D     
#        vec.Set(5)   # Passing values to the function Set
#        print("X: %s, Y: %s" %(vec.x,vec.y))
##        print("X: " + str(vec.x) + ", Y: " + str(vec.y)) #ERROR
#        print("X:",vec.x,"Y:",vec.y,sep=" ")
#  
#if __name__=='__main__': 
#        Main()         


#INHERITACNE
# A Python program to demonstrate working of inheritance 
#class Pet:
#        def __init__(self, name, age):    #__init__ is an constructor in Python    
#                self.name = name 
#                self.age = age   
#
#class Cat(Pet):     # Class Cat inheriting from the class Pet      
#        def __init__(self, name, age): 
#                # calling the super-class function __init__  
#                # using the super() function 
#                super().__init__(name, age)  
#  
#def Main(): 
#        thePet = Pet("Pet", 1) 
#        jess = Cat("Jess", 3) 
#          
#        # isinstance() function to check whether a class is  
#        # inherited from another class 
#        print("Is jess a cat? ",(isinstance(jess, Cat))) 
#        print("Is jess a pet? ",(isinstance(jess, Pet))) 
#        print("Is the pet a cat? ",(isinstance(thePet, Cat))) 
#        print("Is thePet a Pet? ",(isinstance(thePet, Pet))) 
#        print(jess.name) 
#  
#if __name__=='__main__': 
#        Main() 


#GENERATORS
#def Reverse(data): 
#    # this is like counting from 100 to 1 by taking one(-1)   
#    for index in range(len(data)-1, -1, -1):     # step backward.
#        yield data[index] 
#  
#def Main(): 
#    rev = Reverse('Harssh') 
#    for char in rev: 
#        print(char) 
#    data ='Harssh' 
#  
#if __name__=="__main__": 
#    Main() 


##Class variable and instance variable
#class CSStudent: 
#    stream = 'cse'       # Class Variable           
#  
#    def __init__(self, roll):     # The init method or constructor 
#        self.roll = roll        # Instance Variable    
#   
## Objects of CSStudent class 
#a = CSStudent(101) 
#b = CSStudent(102) 
#   
#print(a.stream)  # prints "cse" 
#print(b.stream)  # prints "cse" 
#print(a.roll)    # prints 101 
#   
## Class variables can be accessed using class 
## name also 
#print(CSStudent.stream) # prints "cse"  