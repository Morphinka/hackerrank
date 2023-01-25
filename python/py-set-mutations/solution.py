A_size = int(input())
A = set(map(int, input().split()))
N = int(input()) #number of other sets


for i in range(N):
    operation_length = input()
    splitting = operation_length.split(" ")
    operation = splitting[0]
    length = splitting[1]
    list_of_elements = set(map(int, input().split()))
    
    if "intersection_update" == operation:
        A.intersection_update(list_of_elements)
        
    if "update" == operation:
        A.update(list_of_elements)
        
    elif "symmetric_difference_update" == operation:
        A.symmetric_difference_update(list_of_elements)
        
    elif "difference_update" == operation:
        A.difference_update(list_of_elements)
    else:
        pass
    

print(sum(A))
