import numpy as np


def stickprovsvarians(xs, average=None):
    __average = np.mean(xs) if average is None else average
    return 1 / (len(xs) - (1 if average is None else 0)) * sum([(x - __average) ** 2 for x in xs])


def mk(w_func, ws, xs, expected):
    if isinstance(expected, float) or isinstance(expected, int):
        expected = [expected for _ in range(len(xs))]
    return sum([w_func(w) * (x - e) ** 2 for w, x, e in zip(ws, xs, expected)])


def uppg11_22():
    xs = [
        sum(map(lambda x: (x - 0.184) ** 2, [0.16, 0.18, 0.19, 0.18, 0.21])),
        sum(map(lambda x: (x - 0.232) ** 2, [0.22, 0.21, 0.24, 0.24, 0.25])),
        sum(map(lambda x: (x - 0.158) ** 2, [0.17, 0.15, 0.15, 0.18, 0.14]))
    ]
    print(xs)
    print((sum(map(lambda x: x * 1 / (5 - 1), xs)) / 3) ** (1 / 2))


def square_error(values, expected = None, mute=False):
    if expected is None:
       expected = sum(values) / len(values)

    error = sum([(v - expected) ** 2 for v in values])
    if not mute: print(f"Mean {expected}, Mean square error: {error}")
    return error


def estimate_sigma(A, B, expected):
    return ((square_error(A, expected, mute=True) + square_error(B, expected, mute=True)) / (len(A) + len(B) - 2)) ** (1/2)


def uppgST13():
    A = [12.37, 12.32, 12.41, 12.34, 12.23, 12.36]
    B = [12.41, 12.39, 12.46, 12.35, 12.39, 12.33]
    delta = [b - a for a, b in zip(A, B)]
    square_error(A)
    square_error(B)
    square_error(delta)

def uppgST11():
    uppgST11 = [0.0087, 0.0091, 0.0094, 0.0096, 0.0098, 0.0098]
    square_error(uppgST11)

def uppgST19():
    A = [1493, 1519, 1518, 1517, 1512, 1514, 1489, 1508, 1494]
    B = [1509, 1494, 1512, 1483, 1507, 1491]
    print(estimate_sigma(A, B))
    #delta = [b - a for a, b in zip(A, B)]
    square_error(A)
    square_error(B)
    #square_error(delta)


def uppgST20():
    A = [4.1, 1.5, 1, 2.2, 2.1, 1.2, 2.8, 4, 3.7, 3, 5.6, 3.3]
    B = [4.5, 2.1, 1.9, 2, 2.5, 1.9, 3.4, 4.2, 3.7, 2.9, 5.9, 3.8]
    print(estimate_sigma(A, B))
    delta = [b - a for a, b in zip(A, B)]
    square_error(A)
    square_error(B)
    square_error(delta)


def mean(A): return sum(A)/len(A)


def uppgST21():
    A = [0.25, 0.19, 0.13, 0.23, 0.15, 0.14, 0.24, 0.23, 0.17, 0.15, 0.1, 0.17]
    B = [0.5, 0.28, 0.18, 0.18, 0.34, 0.41, 0.33, 0.26, 0.35, 0.42, 0.22, 0.28]
    delta = [b - a for a, b in zip(A, B)]
    square_error(A)
    square_error(B)
    square_error(delta)

    print(estimate_sigma(A, B, mean(delta)))


if __name__ == "__main__":
    #print(stickprovsvarians([1456.3, 1458.5, 1457.7, 1457.2], average=1457))
    #print(square_error([4.32, 4.22, 4.23, 4.37], 4.285))
    #print(square_error([4.71, 4.63, 4.69, 4.76, 4.58, 4.83]))

    #square_error([0.8, 1.6, 0.9, 0.8, 1.2, 0.4, 0.7, 1.0, 1.2, 1.1,])
    #print(mk(lambda x: x, [1, 1, 1, 1], [8.24, 8.18, 8.15, 8.23], 8.2))
    #print(mk(lambda w: 1/((w/100)**2), [2, 1, 2, 3, 1], [79.1, 80, 81.3, 81.9, 81.7], 80.73))
    uppgST21()
