import numpy as np

N, M = map(int, input().split())

arr = []
for i in range(N):
    A = np.array(list(map(int, input().split())))
    arr.append(A)

print(np.transpose(arr))
print(np.array(arr).flatten())
