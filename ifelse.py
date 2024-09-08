#WAP to write if the given number is negative,positive or zero
x=int(input("Enter a number: "))
if(x>0):
    print(x,"is a positive number")
elif(x<0):
    print(x,"is a negative number")
else:
    print("You entered 0")

#WAP to see weather the enterd number is positive/negative also it is odd or even
y=int(input("Enter a number: "))
if(y>0):
    if(y%2==0):
        print("Number is Positive and Even")
    else:
        print("Number is Positive and Odd")
elif(y<0):
    if(y%2==0):
        print("Number is Negative and Even")
    else:
        print("Number is Negative and Odd")
else:
    print("Number is Zero")
