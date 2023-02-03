import numpy

N = int(input())

AA = []
for i in range(N):
    A = numpy.array(list(map(int, input().split())))
    AA.append(A)
    
BB = []  
for j in range(N):
    B = numpy.array(list(map(int, input().split())))
    BB.append(B)

print(numpy.dot(AA, BB))
