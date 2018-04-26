import helper
import numpy as np

n = 5

# initialize list of students to [0,1,2,3,4]
students = list(range(5))

# randomly generate student preferences
student_prefs = helper.random_preferences(n)

# randomly generate hospital preferences
hospital_prefs = helper.random_preferences(n)

print('Student preferences', student_prefs)
print('Hospital preferences', hospital_prefs)

M = helper.match(student_prefs, hospital_prefs, students)
print(M)
