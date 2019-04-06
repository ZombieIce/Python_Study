filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write('I love programming.\n')
    f.write('I love creating new game.\n')


with open(filename,'a') as f:
    f.write('I also love finding meaning in large datasets.\n')
    f.write('I love creating apps that can run in a browser.\n')
