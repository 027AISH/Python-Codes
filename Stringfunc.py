str1="!!Aishw Arya!!"
print(len(str1))
print("Upper: ",str1.upper())
print("Lower: ",str1.lower())
print("Capitalize: ",str1.capitalize())
print("Rstrip: ",str1.rstrip("!"))
print("Count: ",str1.count("A"))
print("Replace: ",str1.replace("w Arya", "ii"))
print("Split: ",str1.split())
print("Startswith !: ",str1.startswith("!"))
print("Endswith A",str1.endswith("A"))
print("Find: ",str1.find("arry")) #this will give -1 if given is not present
print("Index: ",str1.index("Ary")) #this will give error if the given is not present
#print("isalnum:",str1.iselnum()) #only print true is alphbet and nums presnt else if the puntuations or symbols present then it will print false