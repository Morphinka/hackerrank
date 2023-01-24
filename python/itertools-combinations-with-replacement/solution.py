from itertools import combinations_with_replacement

input = input().split(" ")

S = sorted(input[0])

k = int(input[1])

line = list(combinations_with_replacement(S,k))

for i in line:
    print("".join(i))
