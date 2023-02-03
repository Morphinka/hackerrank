import numpy

N, M = (map(int, input().split()))

A = []
for i in range(N):
    B = numpy.array(list(map(int, input().split())))
    A.append(B)
    
sum_along_0 = numpy.sum(A, axis = 0)   
print(numpy.prod(sum_along_0))
