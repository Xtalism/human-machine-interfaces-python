list = []

for i in range(5):
    list.append(float(input('Enter any number: ')))

list.sort(reverse=True)
print(f'Your sorted array is: {list}')