"""
#2. (Polymorphism with Loop)

Create a class named Bird.
Requirements
Create a method named sound().
It should print:
"Bird makes a sound"

Create another class named Sparrow that inherits from Bird.
Override the sound() method.
It should print:
"Sparrow chirps"

Create another class named Crow that inherits from Bird.
Override the sound() method.
It should print:
"Crow caws"

Create one Sparrow object and one Crow object.
Store both objects inside a list.
Use a for loop to call the sound() method for each object.
"""

class Bird():
    
    def sound(self):
        print(f"Bird makes a sound")
        
class Sparrow(Bird):
    
    def sound(self):
        print(f"Sparrow chirps")

class Crow(Bird):
    
    def sound(self):
        print(f"Crow caws")
        
sparrow1 = Sparrow()
crow1 = Crow()

l = [sparrow1, crow1]
for i in l:
    i.sound()