n=int(input())
ranking=list(map(int,input().split(' ')))[0:n]
m=int(input())
players=list(map(int,input().split()))[0:m]
final_lst=ranking
for values in players:
    final_lst.append(values)
    final_lst = sorted(list(set(final_lst)), reverse=True)
    print(final_lst.index(values)+1)