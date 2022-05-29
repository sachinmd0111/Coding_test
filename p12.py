n,k=map(int,input().split(' '))
value_list=list(map(int,input().split(' ')))
position=0
energy=100
while (position+k)%n!=0:
    if value_list[(position+k)%n]==1:
        energy-=2
    energy-=1
    position+=k
if value_list[(position+k)%n]==0:
    energy-=1
else:
    energy-=3
print(energy)