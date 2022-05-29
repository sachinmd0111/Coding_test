n=int(input("Enter the size of array: "))
temp_list=list(map(int,input().split(' ')))
first_half=sorted(temp_list[0:n//2])
if n&1:
    mid_element=[temp_list[n//2]]
    second_half=mid_element + sorted(temp_list[n//2+1:],reverse=True)
else:
    second_half = sorted(temp_list[n // 2:], reverse=True)
print(first_half+second_half)