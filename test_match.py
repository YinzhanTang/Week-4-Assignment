import helper

# initialize list of students
students = ['A', 'B', 'C']

# initialize student preferences
student_prefs = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['X', 'Y', 'Z']
}

# initialize hospital preferences
hospital_prefs = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['A', 'B', 'C']
}

M = helper.match(student_prefs, hospital_prefs, students)
print(M)
