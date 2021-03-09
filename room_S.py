f = input()


if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a+b+c)/2
    f = p*(p-a)*(p-b)*(p-c)
    S = pow(f, .5)
    print(S)
elif f == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = (a*b)
    print(S)
elif f == 'круг':
    r = int(input())
    p = 3.14
    S = p * r**2
    print(S)
else:
    print("Вы неверно ввели данные.")