#When we pass a reference and change the received reference to something else,
#the connection between passed and received parameter is broken.
#1
#def demo(x):
#    x=[10,20,30]
#
#temp=[1,2,3,4,5]
#demo(temp)
#print(temp) #here value doesn't change as reference is changed in function

##2
#def demo(x):
#    x=[10,20,30]
#
#x=[1,2,3,4,5]
#demo(x)
#print(x) # reference link is broken if we assign a new value (inside the function).

#3
#def myFun(x, y=50):  #default arguments
#    print("x: ", x) 
#    print("y: ", y) 
#myFun(10)
#myFun(10,20)

##4
#def student(firstname, lastname):  
#     print(firstname, lastname)                    
#student(firstname ='Geeks', lastname ='Practice')   # Keyword arguments   
#student(lastname ='Practice', firstname ='Geeks')  

###5
#def myFun(*argv):  # *args for variable number of arguments 
#    for arg in argv:  
#        print (arg) 
#myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

#6
#def myFun(**kwargs):  # *kargs for variable number of keyword arguments 
#    for key, value in kwargs.items():
#        print(value)
#    for value in kwargs.items():
#        print(value)
#    for key, value in kwargs.items(): 
#        print ("%s == %s" %(key, value)) 
## Driver code 
#myFun(first ='Geeks', mid ='for', last='Geeks')   

##7
#Ananoyms Function
#cube = lambda x: x*x*x #lambda keyword is use to create ananonyms function  
#print(cube(7))  

 