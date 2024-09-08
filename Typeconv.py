'''Type Conversions 
Their are two types of type conversions :
1] Conversion = Data type is changed automatically for the conveniance
2] Casting = Data type is changed by user as per requirement
'''
print("Conversion")
a = 10
b = 2.25
print("Type of a",type(a))
print("Type of b",type(b))
sum = a+b
print("Sum :",sum)
print("Converted Type is:",type(sum))

print("Casting")
a = int("6")
print("Changing type of string to interger",type(a))
b = float(7)
print("Changing type of integer to float",type(b))
#c = float("ABC")
#print(c)       Invalid 
#c = int("ABC")
#print(c)       Invalid 