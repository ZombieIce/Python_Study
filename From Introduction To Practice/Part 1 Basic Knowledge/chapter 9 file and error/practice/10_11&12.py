import json


def favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        number = input('What is your favorite number?')
        with open(filename, 'w') as f:
            json.dump(number, f)
        print('I remember your favorite number ' + number + '!')
    else:
        print('I know your favorite number is ' + number + '!')


favorite_number()
