import time
today=int(time.strftime("%H:%M:%S"))
print(today)
h=int(time.strftime("%H"))
if(h<=5 and h==12):
    print("Good Morning!",today)
elif(h<=13 and h==17):
    print("Good AfterNoon!",today)
elif(h<=19 and h==21):
    print("Good Evening!",today)
elif(h<=22 and h==24):
    print("Good Night!",today)
else:
    print("Have a great life")
    
""" print("Current Time is",time.strftime("%H:%M"))
h=int(time.strftime("%H"))
m=int(time.strftime("%M"))
if(h<=11 and m<=59):
    print("Good Morning Sir")
elif(h>=12 and m<=59 and h<17):
    print("Good AfterNoon Sir")
elif(h>=17 and m<=59 and h<21):
    print("Good Evening Sir")
else:
    print("Good Night Sir") """