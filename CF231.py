n=int(input())
contest=[str(input()) for i in range (0,n)]
k0=0
k1=0
pans=0

for j in range (0,n):
    a=contest[j].split()
    for k in range(0,len(a)):
        if a[k]=='1':
            k1+=1
    if k1>=2:
        pans+=1
        k1=0
print(pans)