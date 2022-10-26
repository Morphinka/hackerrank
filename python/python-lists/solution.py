if __name__ == '__main__':
    N = int(input())
     
    my_list =[] 
    
    for i in range(N):
        ele = input()
        my_list.append(ele)
    
    another_list = list()
    for j in my_list:
        a = j.split(' ')
        if len(a) == 3:
            b = [a[0]]
            c = [a[1]]
            cc = [int(item) for item in c]
            d = [a[2]]
            dd = [int(item) for item in d]
        elif len(a) == 2:
            b = [a[0]] 
            c = [a[1]]
            cc = [int(item) for item in c]
        elif len(a) == 1:
            b = [a[0]]
        
        b = b[0]
    
        if b == 'insert':
            another_list.insert(cc[0],dd[0])
        elif b == 'remove':
            another_list.remove(cc[0])
        elif b == 'append':
            another_list.append(cc[0])
        elif b == 'sort':
            another_list.sort()
        elif b == 'pop':
            another_list.pop(-1)
        elif b == 'reverse':
            another_list.reverse()
        elif b == 'print':
            print(another_list)
        else:
            print("Command out of Scope")
