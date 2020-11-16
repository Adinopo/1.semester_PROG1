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




chapter9("tph")
#caesar_cyphher("andrej", 4)
#palindrom("jEleJ")
#cool_methods_chapter8("Andrej", 2, "ej")
