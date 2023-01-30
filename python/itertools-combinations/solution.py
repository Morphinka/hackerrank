from itertools import combinations

S, k = input().split()

for i in range(int(k)):
    for j in list(combinations(sorted(S), i+1)):
        print(''.join(j))
