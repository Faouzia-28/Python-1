print("********Checking eligibility for MAGALIR URIMAI THOGAI*****")
print("Answer the following questions with 'Yes' or 'No'")
print("Are you a female?")
a=input()
a=a.lower()
if a=="yes" :
    print("Are you married?")
    b=input()
    b=b.lower()
    if b=="yes" :
        print("Enter your family income")
        c=int(input())
        if c<450000 :
            print("You are eligible for 'MAGALIR URIMAI THOGAI'")
        else:
            print("You are not eligible for 'MAGALIR URIMAI THOGAI'")
    else:
       print("You are not eligible for 'MAGALIR URIMAI THOGAI'")
else:
    print("You are not eligible for 'MAGALIR URIMAI THOGAI'")

    

