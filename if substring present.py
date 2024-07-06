s = input("Enter the first string: ")
t = input("Enter the second string: ")
s1= 0
t1= 0
while s1 < len(s) and t1 < len(t):
    if s[s1] == t[t1]:
        s1+= 1
    t1+= 1
a = s1 == len(s)
print(a)
