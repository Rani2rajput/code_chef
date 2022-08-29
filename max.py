# x=int(input("enter"))
# y=int(input("enter"))
# z=int(input("enter"))
# a=(x,y,z).sort()
# print(a)


t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    x.sort()
    print(x[1])                             