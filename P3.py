number=int(input("Enter a number "))
count=0
while number>0:
    number//=10
    count+=1
print("The numbers of digits in given number is ",count)