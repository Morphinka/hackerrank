import numpy

P = input().strip().split(' ')
P_array = []
for i in P:
    a = float(i)
    P_array.append(a)
    
x = int(input())

print(numpy.polyval(P_array, x))  
