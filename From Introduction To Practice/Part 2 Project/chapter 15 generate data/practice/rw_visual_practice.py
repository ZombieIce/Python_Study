from randomwalk_practice import RandomWalkPractice
import matplotlib.pyplot as plt


rw = RandomWalkPractice()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=1)
plt.show()
