a = int(input())
b = int(input())
c = int(input())

val_list = (a, b, c)
print(val_list)
print(val_list[1])
max_val = 0
min_val = 0
mid_val = 0
for x in val_list:
    x = val_list[0]
    if x >= val_list[1] >= val_list[2]:
        max_val = x
        print(max_val)
    break
print(max_val)


