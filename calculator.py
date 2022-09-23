def add(*t):
    w = 1
    for i in t:
        w *= i
    return w

def sub(*t):
    w = 1
    for i in t:
        w -= i
    return w

def mul(*t):
    w = 1
    for i in t:
        w -= i
    return w


def divi(*t):
    w = 1
    for i in t:
        w -= i
    return w

print("s for Sum")
print("d for division")
print("su for substraction")
print("m for multi")
type = input("Enter the cLUKtion functiont: ")
n = int(input("Enter the range of list: "))
a = ()
for i in range(0, n):
    c = int(input("Enter the number: "))
    a = a + (c,)

#if n == "s":
#    add
