T = int(input()) #number of test cases

for i in range(T):
     i = input()
     a = i[0]
     b = i[2]
     try:
        c = (int(a)) // (int(b))
        print(c)
     except ZeroDivisionError as d:
        print("Error Code:",d)
     except ValueError as c:
        print("Error Code:",c)
