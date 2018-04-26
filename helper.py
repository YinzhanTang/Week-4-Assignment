def get_ranks(prefs):
    ranks = {} # initialize list of ranks
    for h in prefs:
        rank = {} # initialize list of rank
        for i in range(len(prefs[h])):
            rank[prefs[h][i]] = i+1
            ranks[h] = rank
    return ranks

def match(student_prefs, hospital_prefs, students):
    # Validate if sudents specified in ‘students’ are the same as those in ‘student_prefs’
    while set(students) != set(student_prefs.keys()):
        raise ValuError("The students specified in 'students' are different from those in 'student_prefs'ß")
    # Validate if the number of students and hospitals are the same.
    while len(set(hospital_prefs.keys())) != len(set(student_prefs.keys())):
        raise ValueError("The number of students and hospitals are different")
        # Validate if student preference list is the right length
    for element in student_prefs:
        if len(set(student_prefs[element])) != len(hospital_prefs.keys()):
            raise ValueError('Student preference is not the right length')
        # Validate if each student preference list contains all hospitals.
        if set(student_prefs[element]) != set(hospital_prefs.keys()):
            raise ValuError("Student preference list doesn't contain all hospitals.")
        # Validate if hospital preference list is the right length
    for element in hospital_prefs:
        if len(set(hospital_prefs[element])) != len(student_prefs.keys()):
            raise ValueError('Hospital preference is not the right length')
        # Validate if each student preference list contains all hospitals.
        if set(hospital_prefs[element]) != set(student_prefs.keys()):
            raise ValuError("Hospital preference list doesn't contain all students.")
    # initialize list of free students
    free_students = list(students)
    # initialize student offer lists as reversed prefs
    student_offers = {}
    for element in student_prefs:
        student_offers[element] = list(student_prefs[element])
        student_offers[element].reverse()

    #  call get_ranks function to create the hospital ranks dictionary
    hospital_rank = get_ranks(hospital_prefs)

    M = {} # initialize matching dictionary
    while len(free_students) > 0:
        s = free_students.pop()
        # if s has not proposed to everyone
        if len(student_offers[s]) > 0:
            # get the top remaining preference
            h = student_offers[s].pop()
            # if h is free
            if h not in M:
                M[h] = s
            # if h not free
            else:
                # some pair (s2,h) already exists
                s2 = M[h]
                # compare h's preferences over s and s2
                if hospital_rank[h][s] < hospital_rank[h][s2]:
                    M[h] = s
                    # set s2 free
                    free_students.append(s2)
                else:
                    # s is still free
                    free_students.append(s)
    return M

def random_preferences(n):
    import numpy as np
    prefs = {} # initialize preferences dictionary
    for i in range(n):
        # generate random preference lists
        prefs[i] = list(np.random.permutation(n))
    return prefs

def get_hospital_match_ranks(M, hospital_prefs):
    ranks = {} # initialize preferences dictionary
    hospital_rank = get_ranks(hospital_prefs)
    for i in M:
        ranks[i] = hospital_rank[i][M[i]]
    return ranks

def get_student_match_ranks(M, student_prefs):
    # reverse the dictionary M
    M_rev = {} # initialize reversed dictionary
    for h in M:
        M_rev[M[h]] = h

    ranks = {} # initialize preferences dictionary
    student_rank = get_ranks(student_prefs)
    for i in M_rev:
        ranks[i] = student_rank[i][M_rev[i]]
    return ranks
