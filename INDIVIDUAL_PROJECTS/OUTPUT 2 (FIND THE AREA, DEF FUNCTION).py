#find the area of rectangle, triangle, circle


while True:
    shape = input('Calculate the area of Rectangle, Circle, and Trangle: ')

    if shape == 'Rectangle':

        def area(x, y):
            return x * y

        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))

        Rectangle = area(length, width)

        print(f'The area of the rectangle is {Rectangle}')


    elif shape == 'Triangle':

        def area(x, y):
            return 0.5 * (x * y)

        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))

        Rectangle = area(base, height)

        print(f'The area of the rectangle is {Rectangle}')


    elif shape == 'Circle':

        def area(x):
            return 3.16 * (x ** 2)

        radius = int(input("Enter the radius: "))

        circle = area(radius)

        print(f'The area of the rectangle is {circle}')

    else:
        print('Invalid input')
        continue