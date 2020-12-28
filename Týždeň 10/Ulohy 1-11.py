"""
Exercises from green book and from teacher
Chapter 10
LISTS
"""

from bisect import *
import random, time


# From python documentation about BISECT module
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return print(i, grades[i])


# Rearranging letters in one word u get other word
def is_anagram(word1: str, word2: str):
    if sorted(word1) == sorted(word2):
        return print("Words are anagrams.")
    return print("Words are not anagrams.")


# Prints those elements, that are counted in a list more than 1
def has_duplicates(listik: list):
    i = 0
    while i < len(listik):
        print("Length of a list:", len(listik))
        if listik.count(listik[i]) > 1:
            print("This number ->", listik[i], "appears more than one in the list.")
            the_one = listik[i]
            listik.pop(i)
            for j in range(listik.count(listik[i])):
                pos = listik.index(the_one)
                listik.pop(pos)
        i += 1


# Return most counted item in a list
def funkcia_1():
    num = int(input("Enter numeric value: "))
    mojlist = []
    most = 0
    while num != 0:
        mojlist.append(num)
        if mojlist.count(num) > mojlist.count(most):
            most = num
        num = int(input("Enter numeric value: "))
    print("Most used number is ", most)


# Delete first and last element from list
def chop(my_list: list):
    my_list.pop()
    my_list.pop(0)
    print(my_list)


# Sum of 2 matrix
def sum_matic(matrix_1: list, matrix_2: list):
    if len(matrix_1) == len(matrix_2):
        for i in range(len(matrix_1)):
            if len(matrix_1[i]) != len(matrix_2[i]):
                print("Matrix can not be summed.")
                return

    final_matrix = []
    for i in range(len(matrix_1)):
        help_matrix = []
        for j in range(len(matrix_1[i])):
            help_matrix.append(matrix_1[i][j] + matrix_2[i][j])
        final_matrix.append(help_matrix)

    print(final_matrix)


# Multiplication of 2 matrix
def multiply_matrix(matrix_1: list, matrix_2: list):
    if len(matrix_1[0]) != len(matrix_2):
        print("Matrix can not be multiplied.")
        return

    definitive = 0
    final_matrix = []
    for i in range(len(matrix_1)):
        help_matrix = []
        for j in range(len(matrix_2[0])):
            for q in range(len(matrix_1[0])):
                multiply = matrix_1[i][q] * matrix_2[q][j]
                definitive += multiply
            help_matrix.append(definitive)
            definitive = 0
        final_matrix.append(help_matrix)

    print(final_matrix)


# Finds, whether common intersection of all intervals in "zoznam[[1,2],[0,3]...]" is non-empty set
def prienik_intervalov(zoznam: list):
    final = []
    for i in range(len(zoznam)):
        new_mat = []
        for j in range(zoznam[i][0], zoznam[i][-1] + 1):
            new_mat.append(j)
        final.append(new_mat)
    print(final)

    for i in range(len(final)):
        print(i)
        for j in range(i + 1, len(final)):
            if zoznam[i][-1] in final[j] or zoznam[i][0] in final[j]:
                print("They have intersection.")
            else:
                print("They do not have intersection.")
                # break


# Name suggest everything
def birthday_paradox():
    iterator = 0
    count = 0
    while iterator < 1000:
        birth_list = []
        for i in range(1, 24):
            birth_list.append(random.randint(1, 365))
        birth_list.sort()
        print(birth_list)

        for j in range(1, 22):
            if birth_list[j] == birth_list[j + 1]:
                count += 1

        iterator += 1

    print("There was %d occurrence(s) in 1000 simulations." % count)


def make_word_append():
    words = open(r"C:\Users\Acer-PC\OneDrive\FEI STU\1.semester\Programovanie 1\words.txt")
    newone = []
    for word in words:
        newone.append(word)
    words.close()

def make_word_plus():
    words = open(r"C:\Users\Acer-PC\OneDrive\FEI STU\1.semester\Programovanie 1\words.txt")
    newone = []
    for word in words:
        newone = newone + [word]
    words.close()

# Compare time consumed by using "append" function and using "+" assignment
def timecompare_append_vs_plus():
    start_time = time.time()
    make_word_append()
    elapsed_time = time.time() - start_time
    print("Time with \"append\" assignment is %0.4f seconds." % elapsed_time)

    start_time = time.time()
    make_word_plus()
    elapsed_time = time.time() - start_time
    print("Time with \"plus\" assignment is %0.4f seconds." % elapsed_time)


# Check  if word is in word-list using "bisect" function
def is_in_wordlist(word: str):
    file = open(r"C:\Users\Acer-PC\OneDrive\FEI STU\1.semester\Programovanie 1\words.txt")
    i = 0
    length = len(word)
    while length > 0:
        half = bisect(file, word[i])
        i += 1
        length -= 1
    if word in half:
        print()


# [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# my = [2, 1, 3, 4, 4, 5, 6]
matrix = [[1, 8, 3], [0, 1, 4], [9, 2, 4], [3, 3, 3]]
matrix_2 = [[1, 2, 3, 5, 6], [4, 5, 6, 1, 5], [7, 8, 9, 1, 2]]
intervals = [[0, 3], [2, 6], [7, 9]]
# has_duplicates(my)
# funkcia_1()
# chop(my)
# scitanie_matic(matrix, matrix_2)
# multiply_matrix(matrix, matrix_2)
# prienik_intervalov(intervals)
# birthday_paradox()
timecompare_append_vs_plus()
