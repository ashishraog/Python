#Polymorphism-Having many forms
#1
# len() being used for a string 
print(len("geeks")) 
  
# len() being used for a list 
print(len([10, 20, 30])) 

#2Polymorphism with class method
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi the primary language of India.") 
  
    def typ(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def typ(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA()

#iterates through a tuple of objects. 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.typ()
    
#implementing Polymorphism with Function
def func(obj): 
    obj.capital() 
    obj.language() 
    obj.typ() 
   
func(obj_ind) 
func(obj_usa) 
#3Polymorphism with inheritance  #Method Over-riding
class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): #Method Over-riding
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): #Method Over-riding
    print("Ostriches cannot fly.") 
      
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 
  
obj_bird.intro() 
obj_bird.flight() 
  
obj_spr.intro() 
obj_spr.flight() 
  
obj_ost.intro() 
obj_ost.flight() 

#4 