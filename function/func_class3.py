# Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
# и возвращает функцию, которая также берет два аргумента (числа),
# и возвращает результат умножения аргументов внешней функции плюс результат деления
# аргументов внутренней функции.
# Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)
def chis(a, b):
    return a * b

def chis1(x, y):
  return x / y


print(int(chis(4, 2)) + int(chis1(6, 2)))

