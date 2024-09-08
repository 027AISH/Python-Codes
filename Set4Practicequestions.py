#WAP using functions to give average of 3 numbers
'''def average(a,b,c):
    avg=(a+b+c)/3
    print("Average of three number: ",avg)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
average(a,b,c)'''
#Wap to print the length of list using function
'''numbers=[1,2,3,4,5,6,7]
alphabets=["a","b","c","d","e","f"]
def list_length(list):
    print(len(list))
len_of=input("Numbers or alphabets: ")
list_length(len_of)'''

#WAP to print a list in same line using loops
'''Fruits=["Apple","Banana","Orange"]
print(Fruits)
print("Fruits:",end=" ")
for fruit in Fruits:
    print(fruit,end=" ")'''

#Write a function to find a factorial of n 
'''count=int(input("Enter a number to get factorial: "))
def factorial(count):
    fact=1
    while count>=1:
     fact=fact*count
     count-=1
    print("Factorial:",fact)   
factorial(count)'''

#WAP to convert USD to Rupee
USD=int(input("Enter Dollars: "))
def usd_inr():
    Rupee=USD*83.6246
    print("The Ruppes of",USD,"is:",Rupee)
usd_inr()