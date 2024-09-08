#while loops must be used when thier is some start and stop value which can we change and contains condition
#while loops are not mostly used for programming with numbers but used for conditions
#while loop works for a condition until it is satisfied after it get unsatisfied it changes 
#IN WHILE TEIR IS FIRST = STARTING NUMBER
#SECOND = STOPPING NUMBER(IN WHILE)
#THIRD = PRINT()
#FOURT = INCREMENT OR DECREMENT

#Print hello 5 times using while
""" num=0    #Iterator 
while num<5:    #iterations
    print("hello")
    num=num+1   #end    """

#Print 1 to 27 numbers
""" num=0           #Starting condition
while num<=27:      #stoping condition
    print(num)
    num=num+1 """

#Print 27 to 1 numbers
""" num=27
while num>=1:      #while 27>=1
    print(num)     #print num
    num=num-1      #num = 27-1
 """
#Print multiplication table of number
""" table=int(input("Enter number to get table: "))
num=1
while num<=10:
    print(num*table)
    num=num+1 """

#wap to print elements in a list using while loop
""" nums=[1,2,3,4,5,6]
i=0
while i < 6: #len(nums)-1
    print(nums[i])
    i=i+1   """

#Search for a number x in the tuple
""" tup=(1,4,9,16,25,36,49,64,81,100)
index=0
search=int(input("Enter number to search whether it consist in present tuple: "))
while index < len(tup):
    if search==tup[index]:
        print(tup[index],"is present in this tuple")
    else:
        print("Finding")
    index=index+1     """
#Print sum of all numbers between 1 to n using while loop.
""" summ=0
count=1
natural=int(input("Enter number: "))
while count<=natural:
    summ=summ+count
    count=count+1
print("Sum of first ",natural,"natural numbers is: ",summ) """