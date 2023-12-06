import numpy as np

from matstat import read_messy_input


def square_sum(xs):
    return sum([x ** 2 for x in xs])


def s_xx(xs):
    avg = np.mean(xs)
    return square_sum([x - avg for x in xs])


def s_xy(xs, ys):
    avg_x = np.mean(xs)
    avg_y = np.mean(ys)
    return sum([(x - avg_x) * (y - avg_y) for x, y in zip(xs, ys)])


def linear_regression(xs, ys):
    avg_x = np.mean(xs)
    avg_y = np.mean(ys)

    def line(alfa, beta, x):
        q0 = syy - (sxy ** 2) / sxx
        sigma = np.sqrt(q0 / (len(xs) - 2))
        std = sigma * np.sqrt(1 / len(xs) + ((x - avg_x)**2) / sxx)

        y = alfa + beta * x
        print(f"y({x}) = {y}, {std=}, {sigma=}, {q0=}")
        return y, std

    sxx = s_xx(xs)
    syy = s_xx(ys)
    sxy = s_xy(xs, ys)

    beta_observed = sxy/sxx
    alfa_observed = avg_y - beta_observed * avg_x

    error = 0

    print(f"{sxx=}, {syy=}, {sxy=}, \n{beta_observed=}, {alfa_observed=}, {avg_x=}, {avg_y=}")
    print(f"my_0* = {alfa_observed} + {beta_observed} * x")
    print(f"y* = {alfa_observed} + {beta_observed} * x + {error}")

    return lambda x: line(alfa_observed, beta_observed, x)


if __name__ == "__main__":
    xs = read_messy_input("0,4 0,7 1 1,2 1,4 1,7 2")
    ys = read_messy_input("0,23 0,34 0,42 0,55 0,61 0,77 0,84")
    linear_regression(xs, ys)(1.2)