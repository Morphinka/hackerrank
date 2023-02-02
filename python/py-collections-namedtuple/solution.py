from collections import namedtuple

N = int(input())
columns_names = namedtuple('student', input())
marks_sum = 0

for i in range(N):
    marks_sum += int(columns_names(*input().split()).MARKS)

print(marks_sum / N)
