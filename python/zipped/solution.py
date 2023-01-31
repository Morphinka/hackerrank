N, X = input().split()

all_grades = []
for i in range(int(X)):
    all_grades.append([float(num) for num in input().split()])
    

grades_tuples = zip(*all_grades)
for grade_tuple in grades_tuples:
    print(sum(grade_tuple) / int(X))
