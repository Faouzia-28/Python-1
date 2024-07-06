#finding if the year is leap or not
y=int(input("Enter a year"))
if(y%100==0)and(y%400==0):{#here the century years are leap only if both divisible by 100 and 400
print("year is leap")}
elif(y%4==0)and(y%100!=0):{#here the years without century is calculated
print("year is leap")}
else:{
print("year is not leap")}
