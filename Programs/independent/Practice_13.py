input_words = input('Please enter words separated by commas: ')

def splitArray(string):
        for word in string.split(','):
            print(word)
        return string

splitArray(input_words)