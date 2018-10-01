#!/usr/bin/env python3

# Spearman's rank correlation coefficient
# Given 2 data sets of n elements,  X and Y, calculate the value of Spearman's rank correlation coefficient.


def get_rank(lst):
    _rank = dict((v,i+1) for i, v in enumerate(sorted(set(lst))))
    return [_rank[v] for v in lst]

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rX = get_rank(X)
rY = get_rank(Y)

d = [(rX[i] - rY[i])**2 for i in range(n)]
rxy = 1 - (6*(sum(d)) / (n * (n*n -1)))

print (round(rxy, 3))
