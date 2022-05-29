n=int(input("Enter how many names "))
name_lst=[]
for i in range(n):
    name_lst.append(input())
print(name_lst)

name_lst=sorted(name_lst,key=lambda value:value[0])
print(name_lst)
for name in name_lst:
    print(name)