string=input()
n=int(input())
total=string.count('a')
answer=total*(n//len(string))
answer+=string[:n%len(string)].count('a')
print(answer)