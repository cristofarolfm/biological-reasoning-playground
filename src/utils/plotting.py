import matplotlib.pyplot as plt

def scatter(x, y, title=""):
    plt.figure()
    plt.scatter(x, y)
    plt.title(title or "scatter")
    plt.xlabel("x"); plt.ylabel("y")
    plt.show()
