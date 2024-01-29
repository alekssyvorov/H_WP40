# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end='  ')

# 1*1 = 1 1*2 = 2 ...  1*10 = 10
# a = int(input("A "))
# b = int(input("B "))
# for i in range(a, b+1):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}", end="   ")
#     print()
# Користувач вводить число. Необхідно визначити кількість цифр
# у цьому числі, порахувати їхню суму та середнє арифметичне.
# Визначити кількість нулів у
# цьому числі. Спілкування з користувачем організувати через меню.

b = int(input("A "))
while True:
    a = b
    menu = input("1 - count number\n2 - Suma\n3 - Average\n4 - Zero\n5 - Exit\n")
    if menu == "5":
        break
    if menu == "1":
        count_n = len(str(a))
        count_number = 0
        while a > 0:
            a //= 10
            count_number += 1
        print(count_number)
    elif menu == "2":
        a = b
        suma = 0
        while a > 0:
            t = a % 10 # t %= 10
            a = a // 10 # t //= 10
            suma = suma + t
        print(suma)
    elif menu == "3":
        a = b
        suma = 0
        while a > 0:
            t = a % 10  # t %= 10
            a = a // 10  # t //= 10
            suma = suma + t
        a = b
        count_n = len(str(a))
        average = suma / count_n
        print(average)
    elif menu == "4":
        a = b
        count_zero = 0
        while a > 0:
            t = a % 10
            a //= 10
            if t == 0:
                count_zero += 1
        print(f"count_zero {count_zero}")
        count_zero = 0
        for i in str(a):
            if int(i) == 0:
                count_zero += 1
        print(count_zero)

print()

