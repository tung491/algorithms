import numpy as np


def strassen_mutiply(x, y):
    """
    Muliply 2 matrices using strassen algorithms which base on Divide and Conquer Algorithm
    :param x:
    :param y:
    :return: result
    """
    n = x.shape[0]
    split_n = n // 2
    if n == 1:
        result = x * y
    else:
        a, b = x[:split_n, :split_n], x[:split_n, split_n:]
        c, d = x[split_n:, :split_n], x[split_n:, split_n:]
        e, f = y[:split_n, :split_n], y[:split_n, split_n:]
        g, h = y[split_n:, :split_n], y[split_n:, split_n:]
        p1 = strassen_mutiply(a, f - h)
        p2 = strassen_mutiply(a + b, h)
        p3 = strassen_mutiply(c + d, e)
        p4 = strassen_mutiply(d, g - e)
        p5 = strassen_mutiply(a + d, e + h)
        p6 = strassen_mutiply(b - d, g + h)
        p7 = strassen_mutiply(a - c, e + f)
        result = np.zeros_like(x)
        result[:split_n, :split_n] = p5 + p4 - p2 + p6
        result[:split_n, split_n:] = p1 + p2
        result[split_n:, :split_n] = p3 + p4
        result[split_n:, split_n:] = p1 + p5 - p3 - p7
    return result


def main():
    x = np.array([
        [1, 2],
        [3, 4]
    ])
    y = np.array([
        [5, 6],
        [7, 8]
    ])
    expect = np.dot(x, y)
    result = strassen_mutiply(x, y)
    print(f'Expect: {expect} \n Result: {result}')


if __name__ == '__main__':
    main()
