import numpy

N = int(input())

arr = []
for i in range(N):
    A = numpy.array(list(map(float, input().split())))
    arr.append(A)

result = numpy.linalg.det(arr)
print(round(result,2))
