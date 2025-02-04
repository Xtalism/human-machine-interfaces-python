# Práctica 4, Manuel Piña Olivas - 201060 
import math

x = float(input('Enter x Value: '))
y = float(input('Enter y Value: '))

addition = x + y
substraction = x - y
product = x * y
division = x / y
power = x**y
trigonometric = math.cos(x) + math.sin(x)**2

print('x and y addition = ', addition)
print('x and y substraction = ', substraction)
print('x and y product = ', product)
print('x and y division = ', division)
print('x and y trigonometric = ', trigonometric)