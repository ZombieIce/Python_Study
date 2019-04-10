from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist._x_title = 'Results'
hist._y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
