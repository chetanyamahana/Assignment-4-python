n = int(input("Enter Year: "))
if((n%4==0) and (n%100 != 0))|( (n%100==0) and (n%400==0)):
    print(n," is a Leap Year.")
else:
    print(n," is not a leap year.")