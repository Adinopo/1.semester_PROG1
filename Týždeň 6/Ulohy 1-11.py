'''
Ulohy z týždňa 6
    While cykly
'''

# 1
def vrat_kladne():
    cislo = int(input("Enter number value: "))
    if cislo <= 0:
        print("Sum of positive entered numbers: 0")
        return
    sum = 0
    while cislo > 0:
        sum = sum + cislo
        cislo = int(input("Enter number value: "))
    return print("Sum of positive entered numbers: ", sum)



# 2
def stvorce_mensie(n):
    if n < 0:
        return print("All existing squares are greater then ",n)
    cislo = 0
    while cislo*cislo <= n:
        print(cislo*cislo)
        cislo += 1



# 3
def dva_na_x(n):
    if n > 0:
        cislo = 0
        while pow(2,cislo) <= n:
            cislo += 1
        return print(cislo-1)
    else:
        return print("All 2 powered x are greater then ",n)



# 4
def index_of_greatest():
    cislo = int(input("Enter any number: (for exit, press '0')"))
    if cislo == 0:
        return print("1")
    index = 0
    max_index = 1
    number = cislo
    while cislo != 0:
        index += 1
        if cislo > number:
            max_index = index
            number = cislo
        cislo = int(input("Enter any number: (for exit, press '0')"))
    if number < cislo:
        return print(max_index+1)
    return print(max_index)



# 5
def kolkokrat_vacsie_ako_predchadzajuce():
    cislo = int(input("Enter number value (for exit, press '0'): "))
    if cislo == 0:
        return
    number = cislo
    index = 0
    while cislo != 0:
        if cislo > number:
            index += 1
        number = cislo
        cislo = int(input("Enter number value (for exit, press '0'): "))
    if number < cislo:
        return print(index + 1)
    return print(index)



# 6
def rovne_najvacsiemu_nacitanemu():
    cislo = int(input("Enter number value (for exit, press '0'): "))
    if cislo == 0:
        return
    max = cislo
    index = 0
    while cislo != 0:
        if cislo > max:
            max = cislo
            index = 0
        if max == cislo:
            index += 1
        cislo = int(input("Enter number value (foe exit press '0'): "))
    return print(index)



# 7
def pocet_v_postupnosti():
    cislo = int(input("Enter number value (for exit, press '0'): "))
    if cislo == 0:
        return print("1")
    index = 0
    predosly_index = 0
    predosle_cislo = cislo
    while cislo != 0:

        if cislo == predosle_cislo:
            index += 1

        if predosly_index < index:
            predosly_index = index

        if cislo != predosle_cislo:
            index = 1

        predosle_cislo = cislo
        cislo  = int(input("Enter number value (for exit, press '0'): "))
    return print(predosly_index)



# 8
def fibonacci_index_a(x):
    pass


#pocet_v_postupnosti()
#rovne_najvacsiemu_nacitanemu()
#kolkokrat_vacsie_ako_predchadzajuce()
#index_of_greatest()
#dva_na_x(-16)
#stvorce_mensie(10)
#vrat_kladne()
