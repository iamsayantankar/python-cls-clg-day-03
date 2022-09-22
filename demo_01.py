# def odd(*t):
#     for i in t:
#         if i % 2 == 1:
#             print(i)
#
#
# a = ()
# n = int(input("Enter the range of list: "))
# for i in range(0, n):
#     c = int(input("Enter the number: "))
#     a = a + (c,)
#
# odd(c)


def fact(*t):
    w = 1
    for i in t:
        w *= i
    print(w)


a = ()
n = int(input("Enter the range of list: "))
for i in range(0, n):
    c = int(input("Enter the number: "))
    a = a + (c,)

fact(a)
