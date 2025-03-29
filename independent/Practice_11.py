def temperature_conversion():
    conversion = input('Enter temperature conversion: \nType C to °F\nType F to °C\n->').lower()

    if conversion == 'f':
        fahrenheit = float(input('Please enter your temperature °F: '))
        celsius = (5 / 9) * (fahrenheit - 32)
        print(f'{fahrenheit}°F is equal to {celsius:}°C')
    elif conversion == 'c':
        celsius = float(input('Please enter your temperature °C: '))
        fahrenheit = ((9 / 5) * (celsius)) + 32
        print(f'{celsius}°C is equal to {fahrenheit:}°F')
    else:
        print('Invalid input. Please type "C" or "F".')

temperature_conversion()