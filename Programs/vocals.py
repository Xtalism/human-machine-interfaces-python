phrase = input('Enter a phrase: ')
vocals = ['a', 'e', 'i', 'o', 'u']

for vocal in vocals:
    counter = 0
    for ph in phrase:
        if ph == vocal: counter += 1
    print('Your vocal {} number is: {} '.format(vocal, counter))