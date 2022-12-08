import cmath

if __name__ == '__main__':
    num = complex(input())
    z = complex(num)
        
    ABS = cmath.polar(z)[0] #values of r
    print(ABS)     
    
    phase = cmath.polar(z)[1] #value of fi
    print(phase)
