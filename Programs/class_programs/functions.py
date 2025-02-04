def double(x):
    double_number = x * 2
    print(f'Your double number is: {double_number}')

def add(a, b, c):
    addition = a + b + c
    print(f'Your addition is: {addition}')

def addition(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def sum_one(*num):
    s = 0
    for m in num:
        s += m
    return(s)

double(5)
add(1, 2, 3)
print(addition([1, 2, 3, 4]))
print(sum_one(1, 2, 3, 4))