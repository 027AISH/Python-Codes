#By nesting if to check wheter a person can drive or cannot drive the car
age=int(input("Enter your age:"))
if(age>=18):
    if(age>=80):
        print("Cannot drive")   
    else: 
        print("Can drive")
else:
    print("Cannot drive")