#import math  #library
#
#a = 3.4536  
## using trunc() to print integer after truncating  
#print ("The integral value of number is : ",end="") 
#print (math.trunc(a)) #eliminate alldecimal part 
#  
## using ceil() to print number after ceiling  
#print ("The smallest integer greater than number is : ",end="") 
#print (math.ceil(a)) #least integer greater than the number
#  
## using floor() to print number after flooring  
#print ("The greatest integer smaller than number is : ",end="") 
#print (math.floor(a)) #greatest integer smaller than the number

## importing numpy module 
#np = __import__('numpy', globals(), locals(), [], 0) # it is equivalent to "import numpy"   
## array from numpy 
#a = np.array([1, 2, 3])   
## prints the type 
#print(type(a))
#
#import numpy
#a= numpy.array([1,2,3])
#print(type(a)) 

## from numpy import complex as comp, array as arr 
#np = __import__('numpy', globals(), locals(), ['complex', 'array'], 0) 
#  
#comp = np.complex
#arr = np.array 
#print(type(comp))
#print(type(arr))