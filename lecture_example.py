students = ['A', 'B', 'C']
hospitals = ['X', 'Y', 'Z']

student_prefs = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['X', 'Y', 'Z']
}

hospital_prefs = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['A', 'B', 'C']
}

# initialize student offer lists as reversed prefs
student_offers = {}
for s in student_prefs:
    student_offers[s] = list(student_prefs[s])
    student_offers[s].reverse()

# create hospital rank dictinaries for easy lookup
hospital_rank = {
    'X': {'A':2, 'B':1, 'C':3},
    'Y': {'A':1, 'B':2, 'C':3},
    'Z': {'A':1, 'B':2, 'C':3}
}

free_students = list(students)  # initialize list of free students
M = {}                          # initialize matching dictionary

while len(free_students) > 0:
    s = free_students.pop()
    # if s has not proposed to everyone
    if len(student_offers[s]) > 0:
        # get the top remaining preference
        h = student_offers[s].pop()
        if h not in M:
            M[h] = s
        else:
            s2 = M[h]
            if hospital_rank[h][s] < hospital_rank[h][s2]:
                M[h] = s
                free_students.append(s2)
            else:
                # s is still free
                free_students.append(s)

print(M)

