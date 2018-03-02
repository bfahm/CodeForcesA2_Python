num=int(input())
elem=str(input())
elem=[int (i) for i in elem.split()]
if num==len(elem):
    for j in range (num):
        for i in range (0, len(elem)-1):
            if elem[i]>elem[i+1]:
                elem [i],elem[i+1]=elem[i+1],elem[i]
    elem=' '.join(str(k) for k in elem)
    print(elem)
