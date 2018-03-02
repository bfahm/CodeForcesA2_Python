n,h = map(int,input().strip().split())
a= input()
splitted=[int(n) for n in a.split()]
width=0


if (1<=n<=1000) and (1<=h<=1000):
    for i in range (0,len(splitted)):
        if splitted[i]>h:
            width+=2
        else:width+=1

print(width)