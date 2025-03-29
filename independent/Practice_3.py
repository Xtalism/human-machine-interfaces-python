# Práctica 3, Manuel Piña Olivas - 201060 
weight = float(input('Ingresa tu peso (kg): '))
stature = float(input('Ingresa tu estatura (m): '))

bmi = weight / stature**2

print('Tu índice de masa corporal es:', round(bmi, 2))