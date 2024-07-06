n=int(input("Enter a number"))
fg=0
for i in range(2,n):
    if n%i==0:
        fg=1
if fg==0:
    print("composite")
else:
    print("prime")
