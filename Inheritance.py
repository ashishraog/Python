#Inheritance
#class Person(): 
#    def __init__(self, name): 
#        self.name = name  
#
#    def getName(self):     # To get name 
#        return self.name 
#   
#    def isEmployee(self):    # To check if this person is employee 
#        return False  
#
#class Employee(Person): # Inherited or Sub class (Note Person in bracket)    
#    def isEmployee(self): # Here we return true 
#        return True
#  
#emp = Person("Geek1")  # An Object of Person 
#print(emp.getName(), emp.isEmployee()) 
#  
#emp = Employee("Geek2") # An Object of Employee 
#print(emp.getName(), emp.isEmployee())


#issubclass() and isinstance() #they returns true or false
#class Base(): 
#    pass   # Empty Class   
#class Derived(Base): 
#    pass   # Empty Class 
#  
#print(issubclass(Derived, Base)) 
#print(issubclass(Base, Derived))   
#d = Derived() 
#b = Base()   
#print(isinstance(b, Derived)) # b is not an instance of Derived  
#print(isinstance(d, Base))  # But d is an instance of Base


#Multiple Inheritance
#class Base1(): 
#    def __init__(self): 
#        self.str1 = "Geek1"
#        print("Base1")
#  
#class Base2(): 
#    def __init__(self): 
#        self.str2 = "Geek2"        
#        print("Base2")
#  
#class Derived(Base1, Base2): 
#    def __init__(self): 
#        Base1.__init__(self)  # Calling constructors of Base1 
#        Base2.__init__(self)  # and Base2 classes
#        print("Derived")
#          
#    def printStrs(self): 
#        print(self.str1, self.str2) 
#         
#ob = Derived() 
#ob.printStrs() 


#Access base class member in derived class
#1 using parent class name 
#2 using super()
#class Base(object): 
#    def __init__(self, x, y): 
#        self.x = x  
#        self.y = y
#class Derived(Base): 
#    def __init__(self, x, y, z): 
#        Base.x = x  #using parent class name
#        super().__init__(x,y)  #using super()
#        self.z = z 
#    def printXY(self): 
#       print(Base.x, self.y, self.z)   
#       print(self.x, self.y, self.z)
#d = Derived(10, 20, 30) 
#d.printXY() 





