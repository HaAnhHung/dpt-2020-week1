import math
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    number: float = reduce(op.mul, range(n, n - r, -1), 1)
    denom: float = reduce(op.mul, range(1, r + 1), 1)
    return number // denom


def prob(n, p, N):
    return float(ncr(N, n) * pow(p, n) * pow(1 - p, N - n))


def infoMeasure(n, p, N):
    return 0 - math.log2(prob(n, p, N))


def sumProb(N, p):
    '''
        Ham sumProb co the dung de kiem chung tong xac suat cua phan bo binomial = 1
        sumProb(50, 0.5) = 0.9999999999999991
        sumProb(100, 0.5) : xap xi 1
        sumProb(50, 0.2) = 0.9999857275230759
        sumProb(100, 0.2) = 0.9999999997963016
        sumProb(500, 0.2) : xap xi 1
    '''
    sum: float = 0
    for x in range(0, N + 1):
        sum += prob(x, p, N)
    return sum


def approxEntropy(N, p):
    '''
    approxEntropy(50, 0.5) = 3.8689735330246795
    approxEntropy(10, 0.5) = 2.706428963227331
    approxEntropy(1, 0.5) = 1
    '''
    sum: float = 0
    for x in range(0, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum


if __name__ == '__main__':
    print(sumProb(50, 0.5))
