def li_search(li,n):
    for i in li:
        if i==n:
            return 1
    return -1
li=[]
a=int(input("Enter number of elements in a list: "))
for i in range(a):
    li.append(float(input("Enter a value: ")))
print(li)
n=float(input("Enter target value: "))
s=li_search(li,n)
if s==1:
    print("The value is present in the list")
else:
    print("The value is not present in the list")
