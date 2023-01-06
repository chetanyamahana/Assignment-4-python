marks = int(input("Enter your Marks: "))
if(marks>80):
    print("Your Grade is A.")
elif(marks<=80 and marks>60):
    print("Your Grade is B.") 
elif(marks<=60 and marks>50):
    print("Your Grade is C.")    
elif(marks<=50 and marks>45):
    print("Your Grade is D.")  
elif(marks<=45 and marks>25):
    print("Your Grade is E.")   
elif(marks<=25 and marks>=0):
    print("Your Grade is F.")      
else:
    print("Entered value is invalid.")       
