guests = ['Natasha', 'James', 'Stephen']
for i in guests:
    print('Hello ' + i + ', welcome to my dinner!')

print('\nSorry, James will not take part in the dinner.\n')
guests[1] = 'Will'
for i in guests:
    print('Hello ' + i + ', welcome to my dinner!')

print('\nHello all guests, my table can contain more guests!\n')
guests.insert(0, 'My Love')
guests.insert(2, 'Bob')
guests.append('Micheal')
for i in guests:
    print('Hello ' + i + ', welcome to my dinner!')