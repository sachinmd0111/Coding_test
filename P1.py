n=input("Enter a 5 digit Number ")
ans=""
for i in n:
    if i!='9':
        ans+=str(int(i)+1)
    else:
        ans+='0'
print(ans)