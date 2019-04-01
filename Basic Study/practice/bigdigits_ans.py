import sys

zero = [' * * * ', ' *   * ',  ' *   * ',  ' *   * ', ' * * * ']
one = ['     * ', '     * ', '     * ', '     * ', '     * ']
two = [' * * * ', '     * ', ' * * * ', ' *     ', ' * * * ']
three = [' * * * ', '     * ', ' * * * ', '     * ', ' * * * ']
four = [' *   * ', ' *   * ', ' * * * ', '     * ', '     * ']
five = [' * * * ', ' *     ', ' * * * ', '     * ', ' * * * ']
six = [' *     ', ' *     ', ' * * * ', ' *   * ', ' * * * ']
seven = [' * * * ', '     * ', '     * ', '     * ', '     * ']
eight = [' * * * ', ' *   * ', ' * * * ', ' *   * ', ' * * * ']
nine = [' * * * ', ' *   * ', ' * * * ', '     * ', '     * ']

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = input('Please input an integer:')
    row = 0
    while row < 5:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row].replace('*', str(number)) + '  '
            column += 1
        print(line)
        row += 1
except ValueError as err:
    print(err, 'in', digits)


