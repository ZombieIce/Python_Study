print('Give me two numbers, and I\'ll add them.')
print('Enter \'q\' to quit.')

while True:
    first_num = input('Please input the first number:')
    second_num = input('Please input the second number:')

    if first_num == 'q':
        break
    elif second_num == 'q':
        break
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except TypeError:
        print('Please input numbers')
        continue
    else:
        print('The sum is:' + str(first_num+second_num))

