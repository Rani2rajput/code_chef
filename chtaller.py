n=int(input())
if 1<=n<=1000:
    for i in range(n):
        a,b=map(int,input().split())
        if 100<=a<=200 and 100<=b<=200 and a!=b:
            if a<b:
                print("B")
            else:
                print("A")