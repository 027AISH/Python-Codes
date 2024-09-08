#Indexing = Here by using indexing we can access the particular character from the string
#By using indexing we can only access the char but cannot edit/change it
A="Aishwarya"
print(A[3])
B=A[8]
print(B)

#Slicing slicing helps to access the number of character from the string and can be edited
str1="Aishwarya Kadre"
str2=str1[0:9]
print(str2)
str3=str1[10:16]
print(str3)
str4=str1[10:len(str1)]
print(str4)
str5=str1[:len(str1)]
print(str5)
str6=str1[9:]
print(str6)

#negative slicing
str="aishwarya \n"
print(str[:-1])
print(str[:-7])
print(str[-9:-2])