'''
Ulohy z cvičení na týždeň 5

Rekurzia
'''


def rec_sum_n(n):
    if n == 0:
        return 1
    sum =+ n
    rec_sum_n(n-1)


rec_sum_n(5)
