import json


def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('What is your name?')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print('we\'ll remember you when you come back, ' + username, '!')
    else:
        print('Welcome back, ' + username + '!')


greet_user()
