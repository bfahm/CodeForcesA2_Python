s=str(input())
lowcount=0
for i in s:
    if (i.islower()):
        lowcount+=1
highcount=len(s)-lowcount
if highcount>lowcount:
    print(s.upper())
elif highcount<lowcount:
    print(s.lower())
else:
    print(s.lower())
