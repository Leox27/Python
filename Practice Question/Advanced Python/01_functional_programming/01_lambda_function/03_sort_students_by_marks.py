"""
#3. Sort Students by Marks
students = [
    ("Mayur", 85),
    ("Suraj", 92),
    ("Vishwas", 78),
    ("Varun", 95)
]
"""

students = [
    ("Mayur", 85),
    ("Suraj", 92),
    ("Vishwas", 78),
    ("Varun", 95)
]

sorted_students = sorted(students, key=lambda x: -x[1])
print(sorted_students)
'''
[('Varun', 95), ('Suraj', 92), ('Mayur', 85), ('Vishwas', 78)]
'''
