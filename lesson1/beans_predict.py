import dataset
from matplotlib import pyplot as plt
xs, ys = dataset.get_beans(100)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean size")
plt.ylabel("Toxicity")

plt.scatter(xs, ys)

w = 0.5
y_pre = w * xs
plt.plot(xs, y_pre)

plt.show()

