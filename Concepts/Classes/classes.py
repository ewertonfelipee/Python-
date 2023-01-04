
class Dog:
	
	def __init__(self, name, age): # construtor
		self.name = name
		self.age = age
					
	def sit(self):
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		print(self.name.title() + " rolled over!")
		
mydog = Dog('Ozzy', 2)
yourdog = Dog('Lucy', 3)

print("my dog's name is " + mydog.name.title() + ".")
print("my dog's is " + str(mydog.age) + " years old!")

mydog.sit()

mydog.roll_over()

print("\nyour dog's name is " + yourdog.name.title() + ".")
print("your dog's is " + str(yourdog.age) + " years old!")

yourdog.sit()

"""
# A Sample class with init method  
class Person:  
    
    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
    
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
    
p = Person('Nikhil')  
p.say_hi()

"""
