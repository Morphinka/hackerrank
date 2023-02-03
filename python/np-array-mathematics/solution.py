import numpy

N, M = (map(int, input().split()))

arr1 = []
for i in range(N):
    A = numpy.array(list(map(int, input().split())))
    arr1.append(A)

arr2 = []
for i in range(N):
    B = numpy.array(list(map(int, input().split())))
    arr2.append(B)


print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2)) 
print(numpy.multiply(arr1, arr2)) 
print(numpy.floor_divide(arr1, arr2))
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))
