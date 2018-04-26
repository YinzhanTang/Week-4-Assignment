import helper
import numpy as np

n = 100
# initialize average match rank lists
student_match_avg_rank = []
hospital_match_avg_rank = []

for i in range(1000):
    # initialize list of students to [0,1,2,3...n]
    students = list(range(n))
    # randomly generate student preferences
    student_prefs = helper.random_preferences(n)
    # randomly generate hospital preferences
    hospital_prefs = helper.random_preferences(n)
    # match given preferences
    M = helper.match(student_prefs, hospital_prefs, students)
    # get the ranks of random student preferences
    student_match_rank = helper.get_student_match_ranks(M, student_prefs)
    # get the ranks of random hospital preferences
    hospital_match_rank = helper.get_hospital_match_ranks(M, hospital_prefs)
    # append the average to the respective lists、
    student_match_avg_rank.append(np.mean(list(student_match_rank.values())))
    hospital_match_avg_rank.append(np.mean(list(hospital_match_rank.values())))

print('Average hospital match rank: ', np.mean(hospital_match_avg_rank))
print('Average student match rank: ', np.mean(student_match_avg_rank))
