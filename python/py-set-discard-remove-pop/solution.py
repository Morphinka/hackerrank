n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    list_of_elements = input().split()
    if list_of_elements[0] == "pop":
        s.pop()
    elif list_of_elements[0] == "discard":
        s.discard(int(list_of_elements[1]))
    elif list_of_elements[0] == "remove":
        s.remove(int(list_of_elements[1]))
        
print(sum(s))
