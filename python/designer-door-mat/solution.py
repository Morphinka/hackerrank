# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = input()
    making_list = n.split(" ")
    N = int(making_list[0])
    M = int(making_list[1])
    
    rows = N
    width = M
      
    for i in range (0, int (rows / 2)):
        pattern = ".|." * ((2 * i) + 1)
        print (pattern.center (width, '-'))
      
    print ("WELCOME".center (width, '-'))
      
    i = int (rows / 2)
    while i > 0:
        pattern = ".|." * ((2 * i) - 1)
        print (pattern.center (width, '-'))
        i = i-1
