#for loops are used when we just need to trverse the elements in the tuple,list,string
"""#Example 1: printing 10 natural numbers
for i in range(1,11):
    print(i) """
#Example 2: Python program to print all the even numbers within the given range.
""" ranges=int(input("Enter range:"))
print("Even Numbers: ") 
for i in range(1,ranges):
    if(i%2==0):
        print(i) """

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
""" given_num=int(input("Enter number to get the sum until it: "))
print("The sum of numbers until",given_num,"is: ")
for i in range(1,given_num+1):
    sum=i+1
    print(sum)
 """  #WRONGGGGGGG

#for loop program to itterate through letters 
""" word="ABCDEF"
for i in word:
    print(i)
 """
#for loop range fun
""" for i in range(0,10):
    print(i+2) """
#itterate through list
""" animal=["Cat","Dog","Cow"]
for i in animal:
    print(i)
    for j in i:
        print(j) """
#zip function for parralel print
""" a="Awa"
b="ia"
c="sr"
d="hy"
for i,j,k,l in zip(a,b,c,d):
    print(i,j,k,l) """
#printing tables
""" number=int(input("Enter a number for table: "))
table=%number==0
for mul in range(1,11,number):
    print(mul) """
#wap to print elements in a list using for loop
""" nums=[1,2,3,4,5,6]
for i in nums:
    print(i) """
#wap to print elements in a list using while loop
""" nums=[1,2,3,4,5,6]
x=int(input("Enter the value to check whether it exist: "))
for val in nums:
    if val==x:
        print("The x=",x,"is present in the list")
        break """

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
n=4
for i in range(1,4):
    

print("Sum:",sum)