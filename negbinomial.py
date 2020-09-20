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
    '''
    sumProb(5, 0.5, 1) = 0.96875
    sumProb(5, 0.5, 2) = 0.8125
    '''
    sum: float = 0
    for i in range(r, N + 1):
        sum += prob(r, p, i)
    return sum


def approxEntropy(N, p, r):
    '''
    Ham approxEntropy tinh xap xi entropy cua nguon tin negative binomial, duoc tinh bang tong cua cac xac suat nhan voi luong thong
    tin tuong ung.
    approxEntropy(5, 0.5, 1) = 1.78125
    approxEntropy(5, 0.5, 2) = 1.8278195311147831
    approxEntropy(5, 0.5, 3) = 1.2806390622295665
    approxEntropy(5, 0.5, 4) = 0.625
    '''
    sum = 0
    for i in range(r, N+1):
        sum += infoMeasure(r, p, i) * prob(r, p, i)
    return sum


