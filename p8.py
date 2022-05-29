string = input("Enter a string ")
ind = 0
while ind < len(string) - 2:
    looper = ind + 1
    if string[ind] == string[looper]:
        while string[looper + 1] == string[ind] and looper < len(string):
            looper += 1
            if looper + 1 == len(string):
                break
        if looper - ind >= 2:
            substring = string[ind:looper + 1]
            # print(substring)
            string = string.replace(substring, '')
            ind = -1

    ind += 1
if len(string) > 0:
    print(string)
else:
    print("Empty ")