def find(li,n):
    for i in li:
        if i == n:
            return "index is "+str(li.index(i))
    return "error"
li=[2,3,4,5,6,8,10,9]
n=int(input("enter a number:\n"))
print(find(li,n))
	
