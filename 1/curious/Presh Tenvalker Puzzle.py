for firstDigit in range(10):
    for lastDigit in range(10):
        number = firstDigit*10000+679+lastDigit

        if number % 72 == 0:
            print(number)
