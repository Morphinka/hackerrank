def arrays(arr):
    arr = (numpy.array(arr, float))
    a = numpy.flip(arr)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
