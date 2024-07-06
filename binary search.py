def bi_search(li,n):
    l=0
    r=len(li)-1
    while l<=r:
        m=(l+r)//2
        a=li[m]
        if a==n:
            return m
        elif a<n:
            l=m+1
        else:
            r=m-1
    return -1
li=[]
b=int(input("Enter the length of the list\n"))
for i in range(b):
    li.append(int(input("Enter a value: ")))
n=int(input("Enter the target value\n"))
li.sort()
c=bi_search(li,n)
if c!=-1:
    print("The value is present in the list")
else:
    print("The value is not present in the list")
