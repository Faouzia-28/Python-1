#WRITE A PROGRAM TO PERFORM CALCULATION REALATED TO ARITHMETIC OPERATORS
print("""Enter to perform:
           '+'   for addition
           '-'    for subtraction
           '*'   for multiplication
           '/'   for division
           '**' for exponential
           '%'  for getting remainder
           '//' for floor division""")
s=input()
a=int(input("enter a number "))
b=int(input("enter another number "))
if s=='+':
    print("Sum =",a+b)
elif s=='-':
    print("subtraction=",a-b)
elif s=='*':
    print("Multiplication=",a*b)
elif s=='/':
    print("Division=",a/b)
elif s=='**':
    print("Exponential=",a**b)
elif s=='%':
    print("Remainder=",a%b)
elif s=='//':
    print("Floor division=",a//b)
else:
    print("invalid")
