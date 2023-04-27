#Задача 26:  Посчитать факториал (произведение 1 до N) и 
#треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

num = int(input("Введитете число: "))

def fact(num):
    if num == 1:
        return 1
    return fact(num-1) * num
print(f"Факториал числа равен: {fact(num)}")

def trian(num):
    if num == 1:
        return 1
    return trian(num-1) + num
print(f"Треугольное число равно: {trian(num)}")