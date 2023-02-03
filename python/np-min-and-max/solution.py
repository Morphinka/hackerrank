import numpy

N, M = (map(int, input().split()))

A = []
for i in range(N):
    B = numpy.array(list(map(int, input().split())))
    A.append(B)
    
minimum = numpy.min(A, axis = 1)
print(max(minimum))
