import matplotlib.pyplot as plt

file_path = 'C:/Users/akhil/OneDrive/Desktop/test.txt'

x = []
y = []

with open(file_path, 'r') as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

plt.plot(x, y, color='blue')
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Sample graph!")
plt.show()
