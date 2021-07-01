def FooBar():
    """
    Simple program to print every number from 1 to 100 on a new line, printing 'Foo' instead of the number if it's divisible by 3,
    'Bar' if it's divisible by 5 and 'FooBar' if it's divisible by both.
    """
    for number in range(1, 101):
        # if number is divisble by 3, assign the value 'Foo', else assign an empty string
        foo = 'Foo' if number % 3 == 0 else ''
        # if number is divisble by 5, assign the value 'Bar', else assign an empty string
        bar = 'Bar' if number % 5 == 0 else ''
        # print foo and/or bar if they aren't empty string, otherwise print number
        print(f'{foo}{bar}' or number)


if __name__ == '__main__':
    FooBar()
