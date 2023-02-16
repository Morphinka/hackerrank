import re 

T = int(input())

for i in range(T):
    UID = input()
    if len(re.findall(r'[A-Z]',UID)) >= 2:
        if len(re.findall(r'[0-9]',UID)) >= 3:
            if re.match(r'^[A-Za-z0-9]+$',UID):
                if  len(re.findall(r'(.).*\1',UID)) == 0:
                    if len(UID) == 10:
                        print('Valid')
                        continue
    print('Invalid')
