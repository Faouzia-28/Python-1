#Write an algorithm , pseudocode to read a 5 subject marks and calculate average and Display the Grade of the student
print("enter the marks of 5 subjects")
m1=float(input("subject1: "))
m2=float(input("subject2: "))
m3=float(input("subject3: "))
m4=float(input("subject4: "))
m5=float(input("subject5: "))
print("*******REPORT CARD******")
print("English     ",m1)
print("Maths       ",m2)
print("Physics     ",m3)
print("Chemistry ",m4)
print("Computer ",m5)
avg=(m1+m2+m3+m4+m5)/5
print("Average    ",avg)
if avg>90 and avg<=100 :
  print("Grade is A")
elif avg>80 and avg<=90 :
  print("Grade is B")
elif avg>70 and avg<=80 :
  print("Grade is C")
elif avg>60 and avg<=70 :
  print("Grade is D")
elif avg>=50 and avg<=60 :
  print("Grade is E")
else:
  print("Grade is F")
