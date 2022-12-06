from collections import Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    X = int(input()) #number of shoes
    S = Counter(map(int, input().split())) #shoe sizes list
    N = int(input()) #desired shoe size
    cost = 0
    
    for i in range(N):
        size, price = map(int, input().split())
        if S[size]:
            cost += price
            S[size] -= 1
    print(cost)
