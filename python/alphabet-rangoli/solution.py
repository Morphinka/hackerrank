import string

def print_rangoli(size):
    L = []
    alpha = string.ascii_lowercase
    for i in range(size):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
