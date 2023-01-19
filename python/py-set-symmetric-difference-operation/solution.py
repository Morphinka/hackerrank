a = int(input()) #number of students subscribed to the English newspaper
b = input() #the space separated list of student roll numbers who have subscribed to the English newspaper
c = int(input()) #number of students who have subscribed to the French newspaper
d = input() #the space separated list of student roll numbers who have subscribed to the French newspaper

e = b.split(" ")
f = d.split(" ")
    
s = set(e)
sym_diff = s.symmetric_difference(f)
print(len(sym_diff))
