"""
#4. (Duck Typing)

Create a class named Duck.
Requirements
Create a method named walk().
It should print:
"Duck is walking"

Create another class named Human.
Requirements
Create a method named walk().
It should print:
"Human is walking"

Create a function named start_walk(obj).
Inside the function, call the walk() method.
Create one Duck object and one Human object.
Call the start_walk() function for both objects.
"""

class Duck():
    
    def walk(self):
        print(f"Duck is walking")

class Human():
    
    def walk(self):
        print(f"Human is walking")
        
duck1 = Duck()
human1 = Human()

def start_walk(obj):
    obj.walk()
    
start_walk(duck1)
start_walk(human1)
'''
Duck is walking
Human is walking
'''


"""
Why is this called Duck Typing?

Python doesn't check:
❌ Is obj a Duck?
❌ Is obj a Human?

It only checks:
Does this object have a walk() method?
If yes, it works.

That's why Python says:
"If it walks like a duck and quacks like a duck, treat it as a duck."
In Python, the object's behavior matters, not its type.
"""
