from collections import deque

N = int(input())
d = deque()

for i in range(N):
    data = list(map(str, input().split()))
    method = data[0]
    
    if len(data) > 1:
        value = int(data[1])
        
    if method == "append":
        d.append(value)
    elif method == "appendleft":
        d.appendleft(value)
    elif method == "clear":
        d.clear()
    elif method == "extend":
        d.extend(value)
    elif method == "extendleft":
        d.extendleft(value)
    elif method == "pop":
        d.pop()
    elif method == "popleft":
        d.popleft()
    elif method == "remove":
        d.remove(value)
    elif method == "reverse":
        d.reverse()
    elif method == "rotate":
        d.rotate()

print(*d)
