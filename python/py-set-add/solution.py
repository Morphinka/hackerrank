N = int(input()) #number of country stamps

countries = set()
for i in range(N):
    i = str(input())
    countries.add(i)

print(len(countries))
