sovet=int(input())
parent=int(input())
left = -1
right = sovet+1
mid=(left+right)//2

while (left+1<right) and (parent+mid)*3!=sovet+mid:
    if (parent+mid)*3>sovet+mid:
        right=mid
    else:
        left=mid
    mid = (left + right) // 2
if (left+1==right):
    mid = left
print(mid)





