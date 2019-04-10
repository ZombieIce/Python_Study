import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [i**3 for i in x_values]

x_large_values = list(range(1, 5001))
y_large_values = [i**3 for i in x_large_values]

plt.xlabel('Values', fontsize=14)
plt.ylabel('Cube of Values', fontsize=14)
plt.title('Cube', fontsize=24)

plt.figure(1)
plt.subplot(211)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlGnBu)
plt.figure(1)
plt.subplot(212)
plt.scatter(x_large_values, y_large_values, c=y_large_values, cmap=plt.cm.YlOrRd)

plt.show()
