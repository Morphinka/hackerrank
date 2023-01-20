T = int(input())
for i in range(T):
    a_size, a = int(input()), set(map(int, input().split()))
    b_size, b = int(input()), set(map(int, input().split()))
    print(a.issubset(b))
