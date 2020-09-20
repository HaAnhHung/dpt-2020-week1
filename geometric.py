import math


def prob(n, p):
    return float(p * pow((1 - p), (n - 1)))


def infoMeasure(n, p):
    return float(0 - math.log2(prob(n, p)))


def sumProb(N, p):
    '''
    Ham sumProb co the dung de kiem chung tong xac suat cua phan bo geometric = 1
    Voi input N du lon, ta co ket qua:
    sumProb(50, 0.5) = 0.9999999999999991
    sumProb(100, 0.5) : xap xi 1
    sumProb(50, 0.2) = 0.9999857275230728
    sumProb(100, 0.2) = 0.9999999997962964
    sumProb(500, 0.2) = 0.9999999999999998
    :param N:
    :param p:
    :return:
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += prob(x, p)
    return sum





def approxEntropy(N, p):
    '''
    Ham approxEntropy tinh xap xi entropy cua nguon tin geometric, duoc tinh bang tong cua cac xac suat nhan voi luong thong
    tin tuong ung.
    approxEntropy(2, 0.5) = 1
    approxEntropy(5, 0.5) = 1.78125
    approxEntropy(100, 0.5) = 1.9999999999999998
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += infoMeasure(x, p) * prob(x, p)
    return sum


if __name__ == '__main__':
    print(sumProb(2, 0.5))