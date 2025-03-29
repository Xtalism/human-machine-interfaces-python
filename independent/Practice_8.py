number_list = []

def append_list(listing):
    while True:
        numbers = (float(input('Enter any float number (type -1 to exit): ')))
        
        if numbers == -1.0:
            break
        listing.append(numbers)
    return listing

def list_average(listing):
    length = len(listing)
    _sum = sum(number_list)
    average = 0
    if _sum > 0:
        average = _sum / length
    return average

print(f'Your stored list is: {append_list(number_list)}')
print(f'Your list average is: {list_average(number_list)}')
print(f'Your list addition is: {sum(number_list)}')
print(f'Your data quantity is: {len(number_list)}')