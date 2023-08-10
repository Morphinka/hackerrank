A = set(map(int,input().split()))
N = int(input())

sets_answers = []

for i in range(N):
    i = set(map(int,input().split()))
    if A.issuperset(i) != True:
        is_superset = False
        sets_answers.append(is_superset)
    else:
        is_superset = True
        sets_answers.append(is_superset)
        
print(all(sets_answers))
