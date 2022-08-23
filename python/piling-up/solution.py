
import sys

list_of_lists = []

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)
    
#print(list_of_lists)
T = list_of_lists[0][0]
#print(T)

for i in range(1, 2*T, 2):
    n = list_of_lists[i][0]
    block = list_of_lists[i+1]
    #print(n)
    #print(block)
    result = 'Yes'
    stack = []
    
    while len(block) > 0:
        if block[0] > block[-1]:
            a_ind = 0
            b_ind = -1
        else:
            a_ind = -1
            b_ind = 0
        
        if len(stack) > 0:
            if block[a_ind] <= stack[-1]:
                stack.append(block[a_ind])
                del block[a_ind]
            elif block[b_ind] <= stack[-1]:
                stack.append(block[b_ind])
                del block[b_ind]
            else:
                result = 'No'
                break
        else:
            stack.append(block[a_ind])
        
         
    print(result)
