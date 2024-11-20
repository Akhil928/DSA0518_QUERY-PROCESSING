import matplotlib.pyplot as plt

x = [0, 10, 20, 30, 40, 50]
y = [0, 20, 40, 60, 80, 140]

plt.plot(x, y, color='blue')

plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Draw a line.")

plt.show()
