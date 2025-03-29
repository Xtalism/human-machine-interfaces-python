# import math

# try: 
#     a = int(input('Enter a number: '))
#     if a >= 0:
#         print(f'The number {a} is positive')
#     elif a <= 0:
#         print(f'The number {a} is negative')
    
# except ValueError:
#     print('You must enter an int value number')

# try:
#     age = int(input('Enter your age: \n'))
    
#     if age <= 0: print('Unborn black jewish baby')
#     elif age >= 1 and age <= 17: print('Potential rapist')
#     elif age >= 18 and age <= 64: print('Serial killer')
#     elif age >= 64 and age <= 120: print('Cultist leader')

# except ValueError:
#     print('You must enter an int value number')

# for i in [1, 2, 3, 4, 5, 'Yes', 'Word']:
#     print(f'Your current value is {i}', end=',')

for i in [1, 3, 5, 7]:
    x = i**2 - (i - 1) + (i + 2)
    print(x)

# for i in range(5, 0, -1):
#     print(i)