if __name__ == '__main__':
    python_students = []
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        scores.append(score)
        python_students.append(student)
    
    list_1 = [] 
    for k in scores:
        if k > min(scores):
            list_1.append(k)
    
    sorting = sorted(list_1)
    sec_min = sorting[0]

    names = [] 
    for i in python_students:
        if i[1] == sec_min:
            names.append(i[0])

    for j in sorted(names):
        print(j)
