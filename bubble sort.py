def bubble_sort(li):
    for i in range(1,len(li)):
        for j in range(i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

l=[]
print("Enter values in the list. If enough enter 'exit'")
while True:
    n=input("Enter a value: ")
    if n.lower() =='exit':
        break
    l.append(float(n))
print(l)
print("The sorted list is:",bubble_sort(l))
