number_list = []

def append_list(listing):
    while True:
        numbers = (float(input('Enter float numbers\n(-1 to exit): ')))
      
        if numbers == -1.0:
            break
        listing.append(numbers)    
    return listing
            
def biggest_number(listing):
    print(f'Your biggest number is: {max(listing)}')
    
append_list(number_list)
biggest_number(number_list)