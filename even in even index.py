n=int(input("Enter the no. of elements in the list: "))
li=[]
co=0
ce=0
for i in range(n):
    li.append(int(input()))
print(li)
for i in range(n):
    if i%2==0:
        if li[i]%2!=0:
            co+=1
    else:
        if li[i]%2==0:
            ce+=1
if co>0 or ce>0:
    print("False")
else:
    print("True")


            
            
    
