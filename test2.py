n = int(input())
if 1900 <= n <= 3000:
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                print("Високосный")
            else:
                print("Обычный")
        else:
            print("Високосный")
    else:
        print("Обычный")

else:
    print("Вы задали число не в том диапазоне лет")

