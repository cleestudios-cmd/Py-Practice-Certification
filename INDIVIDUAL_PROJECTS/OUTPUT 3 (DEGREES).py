def to_fahrenheit(cels):
    return cels * 9 / 5 + 32
def to_celsius(fahren):
    return (fahren - 32) * 5/9

while True:
    temp = input('Covert Temperatures [1](F -> C) or [2](C -> F): ')
    
    while True:
        if temp == '1':
            print('Fahrenheit -> Celsius')
            fahrenheit = float(input('Enter: '))
            print(f'{round(to_celsius(fahrenheit), 2)} °C')

        elif temp == '2':
            print('Celsius -> Fahrenheit')
            celsius = float(input('Enter: '))
            print(f'{round(to_fahrenheit(celsius), 2)} °F')
        
        change = input('Type "Change" to switch conversion or press Enter to continue: ')
        if change.lower() == 'change':
            break


                