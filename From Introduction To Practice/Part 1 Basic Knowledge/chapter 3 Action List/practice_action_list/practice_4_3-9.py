for i in range(1, 21):
    print(i)

numbers = [i for i in range(1000001)]
for i in numbers:
    print(i)

print(min(numbers), max(numbers), sum(numbers))

odd_num = [i for i in range(1, 20, 2)]
print(odd_num)

three_times = [i for i in range(3, 30, 3)]
for i in three_times:
    print(i)


cube = [i**3 for i in range(1, 11)]
for i in cube:
    print(i)

