List1=[2,3,4,5,6,2,4]
List2=[]
for i in List1:
    if i not in List2:
        List2.append(i)
print(List2)