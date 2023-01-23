import re 

T = int(input()) #number of test cases

for i in range(T):
    S = input()
    try:
        re.compile(S)
        print(True)
    except Exception:
        print(False)
