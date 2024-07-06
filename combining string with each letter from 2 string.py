#camuassign1
word1 = input("Enter string 1:\n")
word2 = input("Enter string 2:\n")
l1 = len(word1)
l2 = len(word2)
l = max(l1, l2)

for i in range(l):
    if i < l1:
        print(word1[i], end="")
    if i < l2:
        print(word2[i], end="")
