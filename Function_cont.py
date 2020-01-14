##1
##decorator returns functions and have function def inside them
#def messageWithWelcome(str): 
#    # Nested function 
#    def addWelcome(): 
#        return "Welcome to "
#    return  addWelcome() + str# Return concatenation of addWelcome() and str. 
#  
## To get site name to which welcome is added 
#def site(site_name): 
#    return site_name 
#print(messageWithWelcome(site("GeeksforGeeks")))

##2
##Above can also be defined using decorator function as below:
#def decorate_message(fun): 
#    # Nested function 
#    def addWelcome(site_name): 
#        return "Welcome to " + fun(site_name) 
#    # Decorator returns a function 
#    return addWelcome 
#  
#@decorate_message #Decorator
#def site(site_name): 
#    return site_name; 
#  
## This call is equivalent to call to 
## decorate_message() with function 
## site("GeeksforGeeks") as parameter 
#print(site("GeeksforGeeks")) 

##3
#decorator can also be used to attach data
#def attach_data(func): 
#       func.data = 3
#       print("Inside it")
#       return func  
#@attach_data
#def add (x, y): 
#       return x + y 
#   
## This call is equivalent to attach_data() 
## with add() as parameter 
#print(add(2, 3))  
#print(add.data) 

##4
##Class method and static method
#from datetime import date 
#class Person: 
#    def __init__(self, name, age): 
#        self.name = name 
#        self.age = age 
#      
#    # a class method to create a Person object by birth year. 
#    @classmethod
#    def fromBirthYear(cls, name, year): 
#        return cls(name, date.today().year - year) 
#      
#    # a static method to check if a Person is adult or not. 
#    @staticmethod
#    def isAdult(age): 
#        return age > 18
#  
##temp=Person()
#temp(Person("AShish",35))
#person1 = Person('mayank', 21) 
#person2 = Person.fromBirthYear('mayank', 1996) 
#  
#print(person1.age)
#print(person2.age) 
#  
## print the result 
#print(Person.isAdult(22)) 

##5
##Genrator Function
#def simpleGeneratorFun(): 
#    yield 1 # it resumes from the last execution state when function is called again.
#    yield 2 #it behaves same like return .
#    yield 3
#  
#for value in simpleGeneratorFun():  
#    print(value) 

##6
##return multiple values using tuple, dict, list and object of a class 
#class Test: 
#    def __init__(self): 
#        self.str = "Multiple Return using object of class"
#        self.x = 10   
## This function returns an object of Test 
#def fun1(): 
#    return Test() 
  
#t = fun1()  
#print(t.str) 
#print(t.x)
#
#def fun2(): 
#    str = "Multiple return values using tuple"
#    x   = 20
#    return str, x;  # Return tuple, we could also # write (str, x)  
#                   
#str, x = fun2() # Assign returned tuple 
#print(str) 
#print(x) 
#
#def fun3():
#    str ="Multiple return values using list"
#    x = 30
#    return [str, x]
#list=fun3()
#print(list)
#
#def fun4():
#    d= dict();
#    d['str']="Multiple return using dictionary"
#    d['x']= 40
#    return d
#temp=fun4()
#print(temp)

##7
##Partial functions
#from functools import partial
#def f(a,b,c,d):
#    return 1000*a +100*b + 10*c + d
#    
#
#g=partial(f,1,2,3) #define partial func 
#print(g(5)) #assigning value to partial func
#x=partial(f,b=1,c=1,d=1) # when first argument value is not given only
#print(x(7))

##8
#def create_adder(x): 
#    def adder(y): 
#        return x+y   
#    return adder #function return another function
#  
#add_15 = create_adder(15)   
#print(add_15(10)) 

#9




        












