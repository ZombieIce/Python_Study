numbers = []

while True:
    number = input('enter a number or Enter to finish:')
    if number:
        try:
            n = int(number)
        except ValueError as e:
            print(e)
            continue
        numbers.append(int(n))
    else:
        break

print('numbers:', numbers)
print('count = ', len(numbers), 'sum = ', sum(numbers), 'lowest = ', min(numbers), 'highest = ', max(numbers), 'mean = ', sum(numbers) / len(numbers))

