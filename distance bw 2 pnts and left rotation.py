def dist(x1,x2,y1,y2):
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return d

x1=float(input("Enter the value for x1\n"))
x2=float(input("Enter the value for x2\n"))
y1=float(input("Enter the value for y1\n"))
y2=float(input("Enter the value for y2\n"))
print(dist(x1,x2,y1,y2))
x="Circulation"
print(x.center(50,'*'))
li=[]
a=[]
n=int(input("Enter no.of values:\n"))
for i in range(0,n):
    li.append(int(input("Enter a value:\n")))
print(li)
m=int(input("How many circulation:\n"))
for j in range(1,m+1):
    b=li[j:]
    a=b+(li[:j])
print(a)
