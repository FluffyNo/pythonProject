# # arg1 = float(input("Введите что-то там: "))
# # arg2 = float(input("Введите что-то там 2: "))
# # print("Площадь",arg1 * 2 + arg2 * 2)
# # print("Периметр", arg1+arg2 * 2 )
# # print("Площадь", f"{arg1} * 2 + {arg2} * 2 = {arg1 * 2 + arg2 * 2}")
# # print("Периметр", f"{arg1} + {arg2} * 2 = {arg1 + arg2 * 2}")
#
# import math
# #
# # arg1 = int(input('Введите число: '))
# # calc = math.sqrt(arg1)
# # print('Корень:',calc)
# arg1 = float(input('Введите что-то: '))
# print('Ответ', math.pi * arg1)
import math

# y = 2.6777149896256525
a = float(input('Введите A '))
b = float(input('Введите B '))
x = float(input('Введите X '))
print('y =', (math.pow(a, 2*x) + math.pow(b, -x) * math.cos((a+b)*x)) / (x+1))
# print('r =', math.sqrt(math.pow(x, 2) + b) - math.pow(b, 2) * math.sin(x+a)/x)
