#WRITE A PROGRAM TO FIND THE GIVEN NUMBER N IS A FIBONACCI NUMBER AND THE NUMBER N IS LESS THAN OR EQUAL TO 103
n=int(input("Enter a number"))
a=(5*(n**2))+4
b=(5*(n**2))-4
i=1
count=0
while i*i<=a or i*i<=b:
    if i*i==a or i*i==b:
        if n<=103:
            count=1
            break
        else:
            count=2
            break
    i+=1
if count==1:
    print("Fibonacci and less than or equal to 103")
elif count==2:
    print("Fibonacci but not less than or equal to 103")
else:
    print("Not a fibnocci")
        
        
