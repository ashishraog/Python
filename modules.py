#1 Complex number
import cmath 
  
# Initializing real numbers 
x = 5
y = 3
  
# converting x and y into complex number 
z = complex(x,y); 
  
# printing real and imaginary part of complex number 
print(z)
print ("The real part of complex number is : ",end="") 
print (z.real) 
  
print ("The imaginary part of complex number is : ",end="") 
print (z.imag) 

print ("The phase of complex number is : ",end="") 
print (cmath.phase(z)) 

w = cmath.polar(z)   
# printing modulus and argument of polar complex number 
print ("The modulus and argument of polar complex number is : ",end="") 
print (w)   
# converting complex number into rectangular using rect() 
w = cmath.rect(1.4142135623730951, 0.7853981633974483)   
# printing rectangular form of complex number 
print ("The rectangular form of complex number is : ",end="") 
print (w) 

#2 