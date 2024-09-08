#Functions are the block of codes which contains a particular tasks
#Functions are like keywords which are called and should be defined earlier 
#Their is a "Pass" keyword used to write the function defination later
#WAP to make a calculator by creating their functions
""" print("This calculator is made using match case and functions")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def add(a,b):
    add=a+b
    print("Addition is: ",add)
def sub(a,b):
    sub=a-b
    print("Substraction is: ",sub)
def mul(a,b):
    mul=a*b
    print("Multiplication is: ",mul)
def div(a,b):
    div=a/b
    print("Division is: ",div)
print("\nEnter the number of operation you want to perform"
"\n1.Addition"
"\n2.Substraction"
"\n3.Multiplication"
"\n4.Division")

task=int(input("Enter the opration you want to perform: "))
match task: 
    case 1:
        add(a,b)
    case 2:
        sub(a,b)
    case 3:
        mul(a,b)
    case 4:
        div(a,b) """
#In functions their contains a arguments called as function arguments
#Default , Keyword , Required 
#Default argument take the arguments which have been defined at the time of making the function
#Keyword argument take the arguments which can be changed the sequence of brackets
#Required argument takes the arguments whenever it is present if not present anytime it should be mandatory to enter