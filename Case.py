#Match case is 
print("SIMPLE CALCULATOR!")
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("\nSelect the operation to perform"
"\n1.Addition"
"\n2.Substraction"
"\n3.Multiplication"
"\n4.Division"
)
operat=int(input("\nSelect operation: "))
match operat:
    case 1:
        print("Addition:",x+y)
    case 2:
        print("Substraction:",x-y)
    case 3:
        print("Multiplication:",x*y)
    case 4:
        print("Division:",x/y)
    case _:
        print("INVALID OPERATION")