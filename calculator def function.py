def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    print(a)
    print(b)
    return a*b
def div(a,b):
    return a/b
def exp(a,b):
    return a**b
def rem(a,b):
    return a%b
def fd(a,b):
    return a//b
a=float(input("Enter num1:\n"))
b=float(input("Enter num2:\n"))
c=input("Enter '+','-','*','/','**','%','//' to perform corresponding arithmetic operation:\n")
if c=='+':
    print(add(a,b))
elif c=='-':
    if a>b:
        print(sub(a,b))
    elif b>a:
        print(sub(b,a))
    else:
        print(sub(a,b))      
elif c=='*':
    print(mul(b=90,a=23))
elif c=='/':
    print(div(a,b))
elif c=='**':
    print(exp(a,b))
elif c=='%':
    print(rem(a,b))
elif c=='//':
    print(fd(a,b))
else:
    print("Error")
            
      
