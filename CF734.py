n=int(input())
games=input()
myList=list(games)
a=0
d=0
for i in range(0,n):
    if myList[i]=='A':
        a+=1
    if myList[i]=='D':
        d+=1
if a>d:
    print("Anton")
elif d>a:
    print("Danik")
else: print ("Friendship")