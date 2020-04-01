import pandas
import matplotlib.pyplot as plt
import numpy as np
import pygal

fruits = ['apple', 'peach', 'cherry', 'mango', 'orange']
cost = [23.12, 23.34, 33, 56, 4]
qty = [4, 5, 70, 12, 44]
# plt.plot ( x, y, color)
plt.plot(fruits, cost, color='b')
plt.plot(fruits, qty, color='orange')
plt.xlabel("fruits")
plt.ylabel("Cost per kilo")
plt.title("quantity sold")

plt.show()

# using numpy
t = np.arange(0., 50., 2)
plt.plot(t, t, 'o--', t, t**3, 'gs', t, t**2, 'b^')
plt.show()


# using pygal
gr = pygal.Line()
gr.add('Amazon', 76)
gr.add('Ebay', 80)
gr.add('Lazada', 40)
gr.add('Q0010', 10)
gr.render_in_browser()



