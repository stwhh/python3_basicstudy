# -*-coding:utf-8-*-
import os
from math import fabs
from math import fsum


def total(a=5, *numbers, **tuples):
    print("a=", a)
    for numberitem in numbers:
        print("numberitem[{}]={}".format(numbers.index(numberitem), numberitem))

    for tupleitem1, tupleitem2 in tuples.items():
        print(tupleitem1, tupleitem2)


print(os.getcwd())
print(fabs(-16))
print(fsum([1, 2, 3, -5]))
if __name__ == "__main__":
    print("内部自己调用了")
    print(total(10, 1, 2, 3, 4, 5, Jack=1123, John=2231, Inge=1560))
else:
    print("被外部调用了")
