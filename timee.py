#WAP to show time in python output
""" import time
start_time = time.time()
vel=time.time()
print("Time showing in second:",vel)

vel1=time.strftime("%H:%M:%S")   # %Y: Year (4 digits)
print("Time",vel1)               # %m: Month (01-12)
                                 # %d: Day of the month (01-31)
                                 # %H: Hour (00-23)
                                 # %M: Minute (00-59)
                                 # %S: Second (00-59) """
#WAP to greet user as per the time in python
import time
timee=int(time.strftime("%H"))
#print("HOUR:",timee)
name=str(input("Enter your name: "))
if (timee>=6 and timee<12):
    print("Good Morning",name)
elif (timee>=13 and timee<16):
    print("Good Afternoon",name)
elif (timee>=17 and timee<19):
    print("Good Evening",name)
elif (timee>=20 and timee<23):
    print("Good Night",name)