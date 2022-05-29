lower_bound=int(input("Enter the lower bound value "))
upper_bound = int(input("Enter the upper bound value "))
for values in range(lower_bound,upper_bound+1):
    flag=0
    for value in range(2,values):
        if values%value==0:
            flag=1
            break
    if flag==0:
        print(values,end=" ")