'''          a  +  b
    Operand(a,b)     Operator(+)
------------------------------------------------------
Operands: The value on which the Operation occurs
------------------------------------------------------

Operators:The Operation which occurs
1] Arithmatic : +(Add),-(Sub),*(Multiply),/(Divide),%(Mod=Remainder),**(Raise to)

2] Relational : ==(Equal to),!=(Not Equal to),>(Greater than),<(Less than),>=(Greater/equal),<=(Less/Equal) 

3] Assignment : =,+=,(num = 10  num+=40),-= ,*= ,/= ,%= ,**=

4] Logical : &(and),|(or),!(not)
==============================================================='''
print("1] Arithmatic Operators : ")
a=20
b=10
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Remainder",a%b)
print("Power",a**b)

print("2] Relational Operators :(Output = True/False)")
a=50
b=10
print("A==B:",a==b)
print("A<=B:",a<=b)
print("A>=B:",a>=b)
print("A!=B:",a!=b)

print("3] Assignment Operators : ")
num = 10
num = num + 10
print(num)
a = 20
a -= a 
print(a)
b = 30
b /= b
print(b)
c = 40
c %= c
print(c)
d = 5
d **= d
print(d)

print("3] Logical Operators : ")
a=True
b=False
print("A Anding with B :",a & b)
print("A Oring with B :",a | b)
print("A not :",a)