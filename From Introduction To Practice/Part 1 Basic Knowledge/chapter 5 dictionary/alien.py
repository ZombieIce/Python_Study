alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

new_point = alien['points']
print('You just earned ' + str(new_point) + ' points')

alien['x_position'] = 0
alien['y_postion'] = 25
print(alien)

alien_0 = {'x_position': 0, 'y_postion': 25, 'speed': 'medium'}
print('Original x-position:' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))