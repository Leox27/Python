"""
#14. (Diamond Problem)

Create a class named GrandParent.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- family_name
Create a method named display_family().
It should print:
- Family Name

Create a class named Father that inherits from GrandParent.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- father_name
Create a method named display_father().
It should print:
- Family Name
- Father Name

Create another class named Mother that inherits from GrandParent.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- mother_name
Create a method named display_mother().
It should print:
- Family Name
- Mother Name

Create another class named Child that inherits from both Father and Mother.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- child_name
Create a method named display_child().
It should print:
- Family Name
- Father Name
- Mother Name
- Child Name

Create one Child object.
Call display_child().
"""

class GrandParent():
    
    def __init__(self, family_name):
        self.family_name = family_name
        
    def display_family(self):
        print(f"Family Name: {self.family_name}")
        
class Father(GrandParent):
    
    def __init__(self, family_name, father_name):
        GrandParent.__init__(self, family_name)
        self.father_name = father_name
    
    def display_father(self):
        GrandParent.display_family(self)
        print(f"Father Name: {self.father_name}")

class Mother(GrandParent):
    
    def __init__(self, family_name, mother_name):
        GrandParent.__init__(self, family_name)
        self.mother_name = mother_name
    
    def display_mother(self):
        GrandParent.display_family(self)
        print(f"Mother Name: {self.mother_name}")
        
class Child(Father, Mother):
    
    def __init__(self, family_name, father_name, mother_name, child_name):
        Father.__init__(self, family_name, father_name)
        Mother.__init__(self, family_name, mother_name)
        self.child_name = child_name
        
    def display_child(self):
        Father.display_father(self)
        Mother.display_mother(self)
        print(f"Child Name: {self.child_name}")
        
child = Child("Jadhav", "Saudagar", "Rohini", "Mayur")

child.display_child()
'''
Family Name: Jadhav
Father Name: Saudagar
Family Name: Jadhav
Mother Name: Rohini
Child Name: Mayur
'''

print(Child.mro())
'''
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class '__main__.GrandParent'>, <class 'object'>]
'''
