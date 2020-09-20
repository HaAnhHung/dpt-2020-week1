import math
from functools import reduce
import operator as op


def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res


def ncr(n, r):
    r = min(r, n - r)
    number: float = reduce(op.mul, range(n, n - r, -1), 1)
    denom: float = reduce(op.mul, range(1, r + 1), 1)
    return number // denom


def prob(n, p, N):
    return float(ncr(N - 1, n - 1) * pow(p, n) * pow(1 - p, N - n))


def infoMeasure(n, p, N):
    px = prob(n, p, N)
    return 0-math.log2(px)


def sumProb(N, p, r):
    sum: float = 0
    for i in range(r, N + 1):
        sum += prob(r, p, i)
    return sum


def approxEntropy(N, p, r):
    sum = 0
    for i in range(r, N+1):
        sum += infoMeasure(r, p, i) * prob(r, p, i)
    return sum


