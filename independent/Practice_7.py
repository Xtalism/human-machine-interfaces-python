try:
    rows = int(input('Enter row number: '))

    def pyramid(input):
        for i in range(input):
            for j in range(i + 1):
                print('*', end='')
            print()

    pyramid(rows)

except ValueError:
    print('You must enter an int number value!')