x = 25
a = 23
b = 18
c = 23

if x <= 28:
    print("x is less than 28")
else:
    print("x is larger than 28")

if x == 30:
    print("x is equal to 30")
elif x == 25:
    print("x is equal to 25")
else:
    print("x is not equal to 30 or 25")


if a >= 20 and a <= 30:
    print("a is between 20 and 30")
else: 
    print("x is not between 20 and 30")

if b > 20 or b < 10:
    print("b is larger than 20 or less than 10")
else:
    print("b isn't larger than 20 neither less than 10")

if (not(x == c)):
    print("x is not equal to c")