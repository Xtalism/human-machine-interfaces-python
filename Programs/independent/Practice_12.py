number_list = []

def append_list(listing):
    while True:
        numbers = (float(input('Enter float numbers\n(-1 to exit): ')))
      
        if numbers == -1.0:
            break
        
        listing.append(numbers)    
    return listing
        
def highest_number(listing):
    highest = listing[0]

    for value in listing:
        if value > highest:
            highest = value
    return highest
    
append_list(number_list)
print(f'Your highest number is: {highest_number(number_list)}')