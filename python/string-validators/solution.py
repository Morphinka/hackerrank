if __name__ == '__main__':
    s = input()
    
    #alphanumeric
    if any(letter.isalnum() for letter in s):
        print(True)
    else: 
        print(False)
    
    #alphabetical
    if any(letter.isalpha() for letter in s):
        print(True)
    else: 
        print(False)
    
    #digits
    if any(letter.isdigit() for letter in s):
        print(True)
    else: 
        print(False)
    
    #lowercase    
    if any(letter.islower() for letter in s):
        print(True)
    else: 
        print(False)
    
    #uppercase
    if any(letter.isupper() for letter in s):
        print(True)
    else: 
        print(False)
