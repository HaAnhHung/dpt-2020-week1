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
        Voi input N du lon, ta co ket qua:
        sumProb(50, 0.5) = 0.9999999999999991
        sumProb(100, 0.5) : xap xi 1
        sumProb(50, 0.2) = 0.9999857275230759
        sumProb(100, 0.2) = 0.9999999997963016
        sumProb(500, 0.2) : xap xi 1
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += prob(x, p, N)
    return sum


def approxEntropy(N, p):
    '''
        Ham approxEntropy tinh xap xi entropy cua nguon tin binomial, duoc tinh bang tong cua cac xac suat nhan voi luong thong
        tin tuong ung.
        approxEntropy(2, 0.5) = 1
        approxEntropy(5, 0.5) = 2.041942411043098
        approxEntropy(100, 0.5) = 4.369011409223017
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum


