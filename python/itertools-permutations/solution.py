from itertools import permutations

task = input().split(" ")
S = sorted(task[0]) #string
k = int(task[1]) #size

permutation = list(permutations(S,k))

for i in permutation:
    print(''.join(i))
