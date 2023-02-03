def wrapper(f):
    def fun(l):
        numbers = []
        for i in l:
            number = i[-10:]
            a = "+91"+ " "+ number[:5] + " " + number[-5:]
            numbers.append(a)
        for j in sorted(numbers):
            print(j)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
