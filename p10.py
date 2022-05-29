string=input("Enter the string ")
special_characters=['@','#','$','%','&']
sp_char=alphabets=digits=0
for character in string:
    if ord(character)>=65 and ord(character)<=122:
        alphabets+=1
    if  ord(character)>=48 and ord(character)<=57:
        digits+=1
for character in special_characters:
    if character in string:
        sp_char+=1
print(sp_char)
if sp_char==0:
    if digits==0:
        print("Weak Password ")
    else:
        print("Medium password ")
else:
    print("Strong password ")