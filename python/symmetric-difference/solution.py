a = int(input()) 
b = input() 
c = int(input()) 
d = input() 

e = b.split(" ")
f = d.split(" ")
    
s = set(e)
sym_diff = s.symmetric_difference(f)
lis =sorted(map(int,sym_diff), reverse = False)

for i in lis:
    print(i)
