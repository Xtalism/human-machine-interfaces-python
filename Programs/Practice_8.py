number_list = []

def append_list(_list):
    while True:
        numbers = (float(input('Enter any float number (type -1 to exit): ')))
        
        if numbers == -1.0:
            break
        _list.append(numbers)
    return _list

def list_sum(_list):
    sum = 0
    average = 0
    for i in _list:
        sum += i 
    return sum

def list_average(_list):
    length = len(_list)
    sum = list_sum(_list)
    average = 0
    if sum > 0:
        average = sum / length
    return average

print(f'Your stored list is: {append_list(number_list)}')
print(f'Your list average is: {list_average(number_list)}')
print(f'Your list addition is: {list_sum(number_list)}')
print(f'Your data quantity is: {len(number_list)}')