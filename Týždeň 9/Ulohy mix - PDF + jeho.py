'''
Exercises from book as well as teachers own
Chapter 10 (10.1 - 10.9 only)
LISTS
'''
import random

def nested_sum(pole: list):
    sum = 0
    suma_in = 0
    sum_def = 0
    for i in range(len(pole)):
        adon = pole.pop()
        if type(adon) == int:
            sum = sum + adon
        elif type(adon) == list:
            for j in range(len(adon)):
                suma_in = suma_in + adon.pop()
        sum_def = sum + suma_in
    print(sum_def)
    #sum_def += sum(i)



def cumulative_sum(moje_pole: list):
    print(moje_pole[:])
    new_list = []
    temp = 0
    for i in range(len(moje_pole) - 1):
        temp = temp + moje_pole[i]
        new_list.append(temp)
    print(new_list)



def middle(moje_pole: list):
    print(moje_pole)
    moje_pole.pop(0)
    moje_pole.pop(-1)
    print(moje_pole)
    #moje_pole[1:-1]



def is_sorted(moje_pole: list):
    if moje_pole == sorted(moje_pole):
        print("Pole je zoradené správne.")
    else:
        print("Pole nie je zoradené spŕavne.")



def sucet_parne_pozicie(moje_pole: list):
    print(moje_pole)
    print(sum(moje_pole[::2]))



def vacsie_ako_lavy_aj_pravy(moje_pole: list):
    print(moje_pole)
    new_list = []
    sum = 0
    for i in range(len(moje_pole ) - 1):
        if i == 0:
            if moje_pole[0] > moje_pole[1]:
                sum = sum +1
        else:
            if moje_pole[i] > moje_pole[i - 1] and moje_pole[i] > moje_pole[i + 1]:
                sum = sum + 1
    print(sum)



def pocet_roznych(moje_pole: list):
    print(moje_pole)
    sum = 0
    help = 0

    for i in range(len(moje_pole) - 1):
        i = i - help
        if i > len(moje_pole) - 1:
            break
        if moje_pole.count(moje_pole[i]) > 1:
            print(moje_pole.count(moje_pole[i]), "HA", moje_pole[i])
            sum += 1
            help = moje_pole.count(moje_pole[i])
            for j in range(moje_pole.count(moje_pole[i])):
                print(moje_pole.count(moje_pole[i]))
                moje_pole.remove(moje_pole[i])
        else:
            sum += 1
        print("dlzka listu:", len(moje_pole))

    print("Suma je: ",sum)



def prave_raz(moje_pole: list):
    print(moje_pole)
    sum = 0

    for i in range(len(moje_pole) - 1):
        if moje_pole[i] not in moje_pole[i+1:]:
            sum += 1

    print(sum)



def is_anagram(word_1: str, word_2: str):
    print(sorted(word_1) == sorted(word_2))



def randmo_gen():
    moje_pole_2 = random.sample(range(25), 8)
    return moje_pole_2



def main():
    moje_pole = [1, 5, [2, 3], [3, 4, 5], 6]
    vlastne_pole = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]
    #nested_sum(moje_pole)
    #cumulative_sum(randmo_gen())
    #middle(randmo_gen())
    #is_sorted(vlastne_pole)
    #sucet_parne_pozicie(randmo_gen())
    #vacsie_ako_lavy_aj_pravy(randmo_gen())
    #pocet_roznych(vlastne_pole)
    #prave_raz(vlastne_pole)
    #is_anagram("slovo", "lsvoo")


if __name__ == '__main__':
    main()
