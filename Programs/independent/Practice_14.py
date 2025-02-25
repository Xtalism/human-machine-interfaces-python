phrase = input('Enter any phrase:\n')

def stringOperations(string):
    print(f'\nFirst two characters: {string[0:2]}')
    print(f'Last three characters: {string[-3:]}')
    print(f'Each two characters: {string[0::2]}')
    print(f'Inversed character: {string[::-1]}')
    print(f'Straight character: {string} {string[::-1]}')
    return string
    
stringOperations(phrase)