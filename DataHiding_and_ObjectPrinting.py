#DATA HIGING USING double underscore in front (__parameter)
class MyClass: 

    __hiddenVariable = 0    # Hidden member of MyClass 
    
    # A member method that changes  
    # __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 
   
myObject = MyClass()      
myObject.add(2) 
myObject.add(5)  
#print (myObject.__hiddenVariable) # This line causes error 

#Access hidden variable outside class
#class MyClass: 
#
#    __hiddenVariable = 10    # Hidden member of MyClass 
#  
#myObject = MyClass()      
#print(myObject._MyClass__hiddenVariable) 

#Printing objects
class Test: 
    def __init__(self, a, b): #constructor
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: a is %s," "b is %s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) # This calls __str__() #if no str method is present then it use repr method
print([t]) # This calls __repr__()