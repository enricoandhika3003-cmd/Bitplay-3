a = 56

b = 12

a = a+b

b = a-b

a = a-b

print("Swapped: a =", a, " b =", b)

#Swap2Numbers
def swap1(a, b):
    a = a^b
    b = a^b
    a = a^b
    
    print("After swapping: a =", a, " b =", b)

def swap2(a, b):
    a = (a&b) + (a|b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    
    print("After swapping: a =", a, " b =", b)

swap1(56, 12)
swap2(32, 44)

#DivideWithoutDivide
def divide(Dividend, Divisor):
    
    sign = (-1 if((Dividend<0) ^ (Divisor<0)) else 1)
    
    Dividend = abs(Dividend)
    Divisor = abs(Divisor)
    quotient = 0
    temp = 0
    
    for i in range(31, -1, -1):
        
        if (temp + (Divisor << i) <= Dividend):
            temp += Divisor << i
            quotient |= 1 << i
    
    if sign == -1 :
        quotient =- quotient
    return quotient

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print(f"Result of {a} / {b} is {divide(a, b)}")

#Input: a=72, b=3

#Output: 24
