while True:
    n = int(input("Enter a number: "))
    if n <= 0:
        print('Invalid Input')
        continue
    if n == 1:
        print('Sequence Ends; Total Steps: 0')
        continue
    steps = 0
    while True:
        if n % 2 == 0:
            print(f"{n} is Even --> {n}/2")
            n = n // 2
            steps += 1
            if n == 1:
                print(f'Sequence Ends; Total Steps: {steps}')
                break

        elif n % 2 == 1:
            print(f"{n} is Odd --> 3({n}) + 1")
            n = (3 * n) + 1
            steps += 1
            if n == 1:
                print(f'Sequence Ends; Total Steps: {steps}')
                break




