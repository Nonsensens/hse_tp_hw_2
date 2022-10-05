import time
import random
import matplotlib
import matplotlib.pyplot as plt
from main import read_file, _min, _max, _sum, _mult


def test__speed():
    for i in range(0, 100000 + 1, 10000):
        with open('test_speed.txt', 'w') as f:
            s = ''
            for b in range(i + 1):
                s += str(random.randint(1, 100)) + ' '
            f.write(s)
        t_p = time.time()
        file = read_file('test_speed.txt')
        _min(file)
        _max(file)
        _mult(file)
        _sum(file)
        t_n = time.time()
        print(f'Для размера = {i} время = {t_n - t_p}')


def graph__speed():
    arr_x = []
    arr_y = []
    for i in range(0, 100000 + 1, 10000):
        with open('test_speed.txt', 'w') as f:
            s = ''
            for b in range(i + 1):
                s += str(random.randint(1, 100)) + ' '
            f.write(s)
        t_p = time.time()
        file = read_file('test_speed.txt')
        _min(file)
        _max(file)
        _mult(file)
        _sum(file)
        t_n = time.time()
        arr_x.append(i)
        arr_y.append(round(t_n - t_p, 5))
    matplotlib.use('TkAgg')
    plt.plot(arr_x, arr_y)
    plt.show()


if __name__ == '__main__':
    test__speed()
    graph__speed()
