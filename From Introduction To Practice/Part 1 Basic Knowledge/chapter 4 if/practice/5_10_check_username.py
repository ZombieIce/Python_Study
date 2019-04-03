current_users = ['Adam', 'alice', 'Bob', 'Micheal', 'Natasha']
new_users = ['John', 'Jack', 'James', 'Bob', 'Alice']

for new_user in new_users:
    for current_user in current_users:
        if new_user.upper() == current_user.upper():
            print('The username:' + new_user + ' has been taken!')
