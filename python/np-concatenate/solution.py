import numpy

N, M, P = (map(int, input().split()))

arr1 = []
for i in range(N):
    A = numpy.array(list(map(int, input().split())))
    arr1.append(A)
    
arr2 = []
for i in range(M):
    B = numpy.array(list(map(int, input().split())))
    arr2.append(B)

print(numpy.concatenate((arr1, arr2)))  
