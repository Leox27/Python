"""
#11. (Multiple Inheritance)

Create a class named Father.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- father_name
Create a method named display_father().
It should print:
- Father Name

Create another class named Mother.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- mother_name
Create a method named display_mother().
It should print:
- Mother Name

Create another class named Child that inherits from both Father and Mother.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- child_name
Create a method named display_child().
It should print:
- Child Name
- Father Name
- Mother Name

Create one Child object.
Call display_child().
"""

class Father():
    
    def __init__(self, father_name):
        self.father_name = father_name
        
    def display_father(self):
        print(f"Father Name: {self.father_name}")
        
class Mother():
    
    def __init__(self, mother_name):
        self.mother_name = mother_name
        
    def display_mother(self):
        print(f"Mother Name: {self.mother_name}")
        
class Child(Father, Mother):
    
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name
        
    def display_child(self):
        print(f"Child Name: {self.child_name}")
        Father.display_father(self)
        Mother.display_mother(self)
        
child = Child("Saudagar", "Rohini", "Mayur")

child.display_child()
'''
Child Name: Mayur
Father Name: Saudagar
Mother Name: Rohini
'''

# method resolution order (MRO)
print(Child.mro())
'''
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
'''

