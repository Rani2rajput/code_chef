t=int(input(" "))
for i in range(t):
    X,N,K=map(int,input().split())
    if (K>=X*N):
        print("YES")
    else:
        print("NO")