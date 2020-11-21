'''
Exercises from green book
Chapter 8 and 9
STRINGS
'''

def cool_methods_chapter8(word: str, index: int, char: str):
    # index and '6' are optional arguments, starts - ends
    print(word.find(char, index, 6))

    index = 0
    for letter in word:
        print(letter, index, end=", ")
        index += 1

    # Hodnotí abecedne, NIE VELKOSTNE; VELKE PISMENA SU PRED MALYMI
    if word < "cinamon":
        print("\nAlphabeticaly ordered!", word[0], "<", "c")
    else:
        print("Alphabeticaly not ordered!", word[0], ">", "c")

    print(word.join("POVALA"))
    print(word.replace("j", "jko"))

    # If there is no argument .split(), it splits string in whitespaces
    prem = "Jerg,us Labu,da je, sup,er spev,ák."
    print(prem.split(','))

    # If there is no argument in .strip(), it strips/removes whitespaces
    prem_2 = "www.exmple.com"
    print(prem_2.strip("womc."))

    # Swaps/converts lowercase to uppercase and vice versa
    prem_3 = "Male A VELke PiSmEnA"
    print(prem_3.swapcase())


def palindrom(word: str):


    if word.lower() == word[::-1].lower():
        return print("Is palindrom")
    else:
        return print("Not palindrom")


def caesar_cyphher(word: str, offset: int):
    i = 0
    for letter in word:
        print(chr(ord(word[i]) + offset), end="")
        i += 1


def chapter9(forbidden: str):
    qwr = open('words.txt')
    # fin.readlines().strip()

    for line in qwr:
        if len(line) > 20:
            print(line.strip())


    '''qwr = open('words.txt')
    for line in qwr:
        if 'w' in line:
            print(line.strip())'''

    qwr = open("my_words.txt")
    pom = True
    for line in qwr:
        #if line.find(forbidden) != -1:
          #  print(line.strip())
        #if forbidden not in line:
         #   print(line.strip())
        for i in range(len(forbidden)-1):
            if forbidden[i] not in line:
                pom = True
                continue
            else:
                pom = False
                break
        # Iny spôsob
        for letter in line:
            if letter in forbidden:
                pom = False
                break
            else:
                pom = True
        if pom:
            print(line.strip())

    print("\n")

    # Toto ide po riadkoch
    linus = open("my_words.txt")
    for lines in linus:
        if lines.isalpha():
            print(lines.strip())

    # Toto ide po písmenách
    for letter in forbidden:
        print(letter)



# Nejde dobre
def exe_9_7():
    file = open("words.txt")
    sum = 0
    for line in file:
        line = line.strip()
        for char in range(len(line) - 1):
            char = char * 2
            if char >= len(line) - 1:
                break
            if line[char] == line[char + 1]:
                sum += 1
                if sum == 3:
                    print(line)
                    sum = 0
                    break
            else:
                sum = 0



# Picovina na ntu
def exe_9_8():
    pass

# Picovina na ntu
def exe_9_9():
    '''
    vek = 20
    stringo = str(vek).zfill(2)
    print(stringo)

    vek_2 = 2
    strigno = str(vek_2).zfill(2)
    print(strigno[::-1])
    '''
    pass






#exe_9_7()
#chapter9("tph")
#caesar_cyphher("andrej", 4)
#palindrom("jEleJ")
#cool_methods_chapter8("Andrej", 2, "ej")
