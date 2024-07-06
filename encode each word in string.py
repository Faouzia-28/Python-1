#assignment 8
s=input("enter a string: ")
for char in s:
    if char==' ':
        print(" ",end="")
    else:
        print(ord(char),end="")
