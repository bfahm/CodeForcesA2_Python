gend=str(input())
gend=list (gend)
def binarySearch (item,list):
    for i in range (0, len(list)):
        if list[i]==item:
            return True
    return False

newgend=[gend[0]]
gend.pop(0)
while len(gend)>0:
    if binarySearch(gend[0],newgend)==False:
        newgend.append(gend[0])
        gend.pop(0)
    else: gend.pop(0)
if len(newgend)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")