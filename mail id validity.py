#assignment 9
s=input("enter mail id:\n")
l=len(s)
count=0
if s.islower()==True:
    count+=1
for i in range(0,l):
    if s[i]=="@":
        count+=1
    if s[i:]==".com" or s[i:]==".in":
        count+=1

if count==3:
    print("Valid")
else:
    print("Not valid")
    
