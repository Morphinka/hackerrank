import numpy

N, M = map(int, input().split())

my_array = []
for i in range(N):
    A = numpy.array(list(map(float, input().split())))
    my_array.append(A)

    
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0)) 
stan_dev = numpy.std(my_array)
print(round(stan_dev, 11))
