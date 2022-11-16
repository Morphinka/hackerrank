from itertools import product

if __name__ == '__main__':
    A = input()
    AA = A.split(" ")
    AAA = []
    for i in AA:
        i = int(i)
        AAA.append(i)
    
    B = input()
    BB = B.split(" ")
    BBB = []
    for j in BB:
        j = int(j)
        BBB.append(j)

    cartesian_product = list(product(AAA,BBB))
    print(str([ each for each in cartesian_product ])[1:-1].replace(", (", " ("))
