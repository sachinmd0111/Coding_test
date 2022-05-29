n=input("Enter a 4 digit number ")
multiplier=10**(len(n)-1)
for value in n:
    print(value + '*' + str(multiplier) + ' = ' + str(int(value)*multiplier))
    multiplier//=10