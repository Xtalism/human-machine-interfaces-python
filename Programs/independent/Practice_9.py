number = int(input('Enter an int value number: '))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1
    
print(f'The factorial of {number} is: \n {factorial}')