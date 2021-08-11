import dataset
from matplotlib import pyplot as plt

xs, ys = dataset.get_beans(100)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean size")
plt.ylabel("Toxicity")

plt.scatter(xs, ys)

w = 0.1
alpha = 0.01
for j in range(1000):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre_ = w * x
        e = y - y_pre_
        w = w + alpha * e * x

y_pre = w * xs
plt.plot(xs, y_pre)
plt.show()
print(w)
