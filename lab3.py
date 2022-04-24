import numpy as np
import matplotlib.pyplot as plt

#zad 1 
a = np.array([[1, 2], [3, 4]])
print(a)


def add_padding(a, x):
    new_column = [[x], [x]]
    b = np.append(a, new_column, axis=1)
    print(b)


add_padding(a, -4)


#zad 2
def normalize(a):
    i = 1
    j = 1
    rows = len(a)
    column = len(a[0])
    sumDz = 0
    R = np.zeros((rows, column))
    for i in range(rows):
        sumDz = (sumDz + (a[i][j]) ** 2) ** 1 / 2
        for j in range(column):
            R[i][j] = a[i][j] / sumDz

    print(R)


normalize(a)

#zad 3

def first_composition(n):
    i = 0
    j = 0
    g = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                g[i][j] = 0
            elif i > j:
                g[i][j] = 1
            else:
                g[i][j] = -1
    print(g)


first_composition(5)

#zad 4

def second_composition(n):
    i = 0
    j = 0
    h = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i < j:
                h[i][j] = -1
            else:
                h[i][j] = i + 1

    print(h)


second_composition(5)

#zad 5

def third_composition(n):
    a = np.zeros((n, n))
    a[:n // 2, :n //2] = np.ones_like(a[:n // 2, :n //2])
    a[n // 2:, n //2:] = -np.ones_like(a[:n // 2, :n //2])
    a[n // 2:, :n //2] = np.ones_like(a[:n // 2, :n //2]) * 2
    a[:n //2, n // 2:] = np.ones_like(a[:n // 2, :n //2]) * -2
    
    print(a)

third_composition(4)





#zad 6
# https://www.geeksforgeeks.org/plot-multiple-lines-in-matplotlib/

def simple_plot(a, b):
    plt.plot(a, b, label="line a", color='red', linestyle='dashed')
    plt.plot(b, a, label="line b", color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("podpis wykresu")
    plt.grid(color='green', linestyle='dashed', alpha=0.5, linewidth=1.15)
    plt.legend()
    plt.show()


a = [10, 20, 30, 40, 50]
b = [30, 30, 30, 30, 30]


simple_plot(a,b)

#zad 7
# https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
def func_plot(vmin, vmax, step):
    x = np.linspace(vmin, vmax, step)
    y = ((x ** 2) - (x * 4)) + 8

    # Ustawianie osi na srodku
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.show()


vmin = -50
vmax = 50
step = 100


func_plot(vmin,vmax,step)

#zad 8

def multi_plot(sizes, labels):
    # fig, axs = plt.subplots(2)
    # axs[0].pie(sizes, labels=mylabels)
    # axs[1].bar(mylabels, sizes)
    # plt.show()

    plt.pie(sizes, labels=mylabels)
    plt.figure()
    plt.bar(mylabels, sizes)
    plt.show()


sizes = np.array([1, 2, 3])
mylabels = ['var1',
            'var2',
            'var3']


multi_plot(sizes,mylabels)

#zad 9

def scatter_plot(a, b):
    x1 = np.random.randint(a, b, 10)
    x2 = np.random.randint(a, b, 10)
    y1 = np.random.randint(a, b, 10)
    y2 = np.random.randint(a, b, 10)
    plt.scatter(x1, y1, marker='.', s=9, c='g')
    plt.scatter(x2, y2, marker='o', s=12, c='y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


scatter_plot(1,20)

#zad 10
def make_3D(x, y):
    ax = plt.figure().add_subplot(projection='3d')
    x = np.linspace(0, 1, 100)
    y = (x ** 2 + y ** 2) ** 1 / 2
    ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    return 0

make_3D(1,5)

#Artur Kruszko lab3 