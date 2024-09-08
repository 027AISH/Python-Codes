#Break and Continue 
#break - it breaks the loop after condition is true
#Continue - it skips the particular number as soon as the condition is true

#not workinggggggggggggggg
#Print sum of all even numbers between 1 to n using while loop use break or continue statement
""" count=1
sum1=0
num=int(input("Enter number: "))
while count<=num:
    if count%2==0:
        sum1=sum1+count
        print(sum1)
    count=count+1 """

#wap to break a statement in between count if you reached the enterd number use break
""" count=1
while count<=10:
    if(count==5):
        print("We have reached to Middle number:",count)
    count=count+1 """

#Wap using continue statement
""" count=1
while count<=10:
    if (count==5):
        count=count+1
        continue
    print(count)
    count=count+1 """
#Wap to just print even values n not odd ones
count=0
while count<=10:
    if(count%2!=0):
        count+=1
        continue
    print("Even numbers are: ",count)
    count+=1