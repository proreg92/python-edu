import logging

logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# \
    %(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG
)


class MyClass(object):
    pass


# print(MyClass, type(MyClass), MyClass.__bases__)
m = MyClass()
# m.attr = '123'
n = MyClass()

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l1

# print(l1)
# l1.append(4)
# print(l1)
# print(l3)

k = m
# print(m is k)


# print(l1 == l2)
# print(l3 == l2)
# print(l1 is l3)
# print(m is n)
# print(m, type(m), m.__class__)

class Human:
    pass


h = Human()
h.name = 'John'
h.age = 42


def print_human(human):
    print(Human)
    print(human.name, human.age)


print_human(h)

