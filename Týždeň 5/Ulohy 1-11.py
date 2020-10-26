'''
Ulohy z cvičení na týždeň 5

Rekurzia
'''

# 1
def rec_sum_n(n):
    if n == 1:
        return 1
    else:
        sum = rec_sum_n(n-1)
        result = sum + n
        return result


# 2
def recur_sum_n(n):
    if n > 1:
        sum = recur_sum_n(n-1)
        cislo = int(input("Enter any positive number: "))
        return (cislo + sum)
    else:
        cislo = int(input("Enter any positive number: "))
        return cislo


# 3
def rec_parne(n):
    if n >= 1:
        sum = rec_parne(n-1)
        cislo = int(input("Enter any positive number: "))
        if cislo % 2 == 0:
            return (sum + 1)
        else:
            return sum
    else:
        return 0


# 4
def rec_max(n):
    if n == 1:
        max = int(input("Enter positive number: "))
        return max
    else:
        max = rec_max(n-1)
        cislo = int(input("Enter positive number: "))
        if cislo > max:
            max = cislo
        return max


# 5
def rec_sum_parne(n):
    if n == 1:
        cislo = int(input("Enter positive number: "))
        if cislo % 2 == 0:
            return True
        else:
            return False
    else:
        cislo = rec_sum_parne(n-1)
        cislo2 = int(input("Enter positive number: "))
        if cislo2 % 2 == 0:
            if cislo is True:
                return True
            else:
                return False
        else:
            if cislo is True:
                return False
            else:
                return True

# 6
def rec_sum_prvocisla(n):
    if n == 2:
        return 2
    else:
        cislo = rec_sum_prvocisla(n-1)
        for i in range(2,n):
            if n % i == 0:
                sum = True
                break
            else:
                sum = False
        if sum is False:
            return cislo + n
        else:
            return cislo

# 7 Tower of Hanoi - video (hard)


# 8 - 11 Exercises from pdf book



print(rec_sum_prvocisla(15))
#print(rec_sum_parne(5))
#print(rec_max(5))
#print("Pocet parnych je " , rec_parne(5))
#print(recur_sum_n(5))
#print(rec_sum_n(5))


