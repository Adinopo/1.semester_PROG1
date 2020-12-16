'''
20 bodov
Termín: 13.12. 23:59:59
https://uim.fei.stuba.sk/wp-content/uploads/2020/11/PROG1_projekt2020.pdf

Copyright 2020 Andrej Povala ©
'''


from random import randrange
import time


# Creates matrix and fulfill a list
def gensachovnicu(n: int):
    list_first = []

    for row in range(n+1):
        pom = []
        for column in range(n+1):
            if column == row == 0:
                pom.append([" "])
            else:
                if column == 0:
                    pom.append([str((row-1) % 10)])
                elif row == 0:
                    pom.append([str((column-1) % 10)])
                elif column == (n//2)+1 and (row == 1 or row == n):
                    pom.append(["*"])
                elif 0 < row < n//2 and (column == n//2 or column == (n//2)+2):
                    pom.append(["*"])
                elif row == (n//2)+1 and (column == 1 or column == n):
                    pom.append(["*"])
                elif (row == (n//2)+2 or row == (n//2) and column > 0) and column != (n//2)+1:
                    pom.append(["*"])
                elif row > (n//2)+2 and (column == n//2 or column == (n//2)+2):
                    pom.append(["*"])
                elif row == (n//2)+1 and column == (n//2)+1:
                    pom.append(["X"])
                elif row > 1 and row != (n//2)+1 and column == (n//2)+1:
                    pom.append(["D"])
                elif row == (n//2)+1 and column > 1 and column != (n//2)+1:
                    pom.append(["D"])
                else:
                    pom.append([" "])
        list_first.append(pom)

    return list_first


# Calculating initial movement
def cal_init_move(list_first: list, number: int):
    lenght = (len(list_first[0]) // 2) - 2
    column = (len(list_first[0]) // 2) + 1

    if number <= lenght:
        list_first[number + 1][column] = ['X']
        list_first[1][column] = ['*']
        return (number + 1), column
    elif number <= lenght * 2:
        list_first[lenght + 1][(len(list_first[0]) // 2) + (number - lenght) + 1] = ['X']
        list_first[1][column] = ['*']
        return (lenght + 1), ((len(list_first[0]) // 2) + (number - lenght) + 1)
    elif number <= (lenght * 2) + 2:
        list_first[lenght + (number - lenght) - 1][len(list_first[0]) - 1] = ['X']
        list_first[1][column] = ['*']
        return (lenght + (number - lenght) - 1), (len(list_first[0]) - 1)


# Main function to calculate movement of avatar
def main_move(list_first: list, row_pos: int, column_pos: int, number: int):
    lenght = (len(list_first[0]) // 2) - 2              # len(list_first[0]) // 2 -> middle of the playground

    if column_pos == len(list_first) - 1:
        if number <= ((len(list_first[0]) // 2) + 1) - row_pos:
            list_first[row_pos + number][column_pos] = ['X']    # Sets new avatar´s position
            list_first[row_pos][column_pos] = ['*']             # Overwrites previous avatar´s position with *
            return (row_pos + number), column_pos               # Returning new avatar´s positions in matrix
        elif number >= ((len(list_first[0]) // 2) + 1) - row_pos and len(list_first[0]) - number > len(list_first[0]) // 2:
            list_first[(len(list_first[0]) // 2) + 1][(len(list_first[0]) - 1) - (number - (((len(list_first[0]) // 2) + 1) - row_pos))] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return ((len(list_first[0]) // 2) + 1), ((len(list_first[0]) - 1) - (number - (((len(list_first[0]) // 2) + 1) - row_pos)))
        elif number >= ((len(list_first[0]) // 2) + 1) - row_pos and (len(list_first[0]) // 2 + (number - ((((len(list_first[0]) // 2) + 1) - row_pos) + lenght))) <= len(list_first[0]) - 1:
            list_first[(len(list_first[0]) // 2 + (number - ((((len(list_first[0]) // 2) + 1) - row_pos) + lenght)))][(len(list_first) // 2) + 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + (number - ((((len(list_first[0]) // 2) + 1) - row_pos) + lenght))), ((len(list_first) // 2) + 1)
        else:
            list_first[len(list_first[0]) - 1][len(list_first[0]) // 2 + 1 - (number - ((((len(list_first[0]) // 2) + 1) - row_pos) + (2 * lenght)))] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 1), (len(list_first[0]) // 2 + 1 - (number - ((((len(list_first[0]) // 2) + 1) - row_pos) + (2 * lenght))))
    if 1 <= row_pos < len(list_first[0]) // 2 - 1:
        if (len(list_first[0]) // 2) - 1 >= number + row_pos:
            list_first[row_pos + number][column_pos] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (row_pos + number), column_pos
        elif (len(list_first[0]) // 2) - 1 <= number + row_pos and (len(list_first[0]) - 1) >= (number - (((len(list_first[0]) // 2) - 1) - row_pos)) + len(list_first[0]) // 2 + 1:
            list_first[len(list_first[0]) // 2 - 1][(number - (((len(list_first[0]) // 2) - 1) - row_pos)) + (len(list_first[0]) // 2) + 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 - 1), ((number - (((len(list_first[0]) // 2) - 1) - row_pos)) + (len(list_first[0]) // 2) + 1)
        elif (len(list_first[0]) // 2) - 1 <= number + row_pos and len(list_first[0]) // 2 + 2 >= (number - ((len(list_first[0]) // 2 - 1) - row_pos)) + lenght:
            list_first[(len(list_first[0]) // 2 - 1) + ((number - (((len(list_first[0]) // 2) - 1) - row_pos)) - lenght)][len(list_first[0]) - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return ((len(list_first[0]) // 2 - 1) + ((number - (((len(list_first[0]) // 2) - 1) - row_pos)) - lenght)), (len(list_first[0]) - 1)
        else:
            list_first[len(list_first[0]) // 2 + 1][len(list_first[0]) - 2] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1), (len(list_first[0]) - 2)
    if row_pos == len(list_first[0]) // 2 - 1:
        if number + len(list_first[0]) // 2 + 1 <= len(list_first[0]) - 1:
            list_first[row_pos][len(list_first[0]) // 2 + 1 + number] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return row_pos, (len(list_first[0]) // 2 + 1 + number)
        elif (len(list_first[0]) // 2 - 1) + (number - lenght) <= len(list_first[0]) // 2 + 1:
            list_first[(len(list_first[0]) // 2 - 1) + (number - lenght)][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return ((len(list_first[0]) // 2 - 1) + (number - lenght)), (len(list_first[0]) // 2 - 1)
        else:
            list_first[len(list_first[0]) // 2 + 1][len(list_first[0]) - 1 - (number - 2 * lenght)] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1), (len(list_first[0]) - 1 - (number - 2 * lenght))
    if row_pos == 5 and column_pos == 6:
        if number == 1:
            list_first[row_pos][column_pos - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return row_pos, (column_pos - 1)
        elif number <= 3:
            list_first[len(list_first[0]) // 2 + number][column_pos - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + number), (column_pos - 1)
        elif number <= 5:
            list_first[len(list_first[0]) - 1][(len(list_first[0]) // 2 + 1) - (number - lenght - 1)] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 1), ((len(list_first[0]) // 2 + 1) - (number - lenght - 1))
        else:
            list_first[len(list_first[0]) - 2][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 2), (len(list_first[0]) // 2 - 1)
    if len(list_first[0]) // 2 + 1 <= row_pos <= len(list_first[0]) - 1 and column_pos == len(list_first[0]) // 2 + 1:
        if len(list_first[0]) // 2 + 1 + number <= len(list_first[0]) - 1:
            list_first[len(list_first[0]) // 2 + 1 + number][len(list_first[0]) // 2 + 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1 + number), (len(list_first[0]) // 2 + 1)
        elif len(list_first[0]) // 2 - 1 > (number - lenght):
            list_first[len(list_first[0]) - 1][(len(list_first[0]) // 2 + 1) - (number - lenght)] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 1), ((len(list_first[0]) // 2 + 1) - (number - lenght))
        else:
            list_first[len(list_first[0]) - 1 - (number - 2 * lenght)][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 1 - (number - 2 * lenght)), (len(list_first[0]) // 2 - 1)
    if row_pos == len(list_first[0]) - 1 and column_pos == len(list_first[0]) // 2:
        if number == 1:
            list_first[len(list_first[0]) - 1][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) - 1), (len(list_first[0]) // 2 - 1)
        elif len(list_first[0]) - 1 - (number - 1) >= len(list_first[0]) // 2 + 1:
            list_first[(len(list_first[0]) - 1) - (number - 1)][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return ((len(list_first[0]) - 1) - (number - 1)), (len(list_first[0]) // 2 - 1)
        elif len(list_first[0]) - 1 >= len(list_first[0]) // 2 + (number - lenght):
            list_first[len(list_first[0]) // 2 + 1][len(list_first[0]) // 2 + (number - lenght)] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1), (len(list_first[0]) // 2 + (number - lenght))
        else:
            list_first[(len(list_first[0]) // 2 + 1) - ((number - 2 * lenght) - 1)][1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1 + (number - 2 * lenght - 1)), 1
    if column_pos == len(list_first[0]) // 2 - 1 and len(list_first[0]) // 2 < row_pos <= len(list_first[0]) - 1:
        if row_pos - number >= len(list_first[0]) // 2 + 1:
            list_first[row_pos - number][len(list_first[0]) // 2 - 1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (row_pos - number), (len(list_first[0]) // 2 - 1)
        elif len(list_first[0]) // 2 + 1 <= (len(list_first[0]) - 1 - (number - (row_pos - len(list_first[0]) // 2 + 1))) and 1 <= (len(list_first[0]) // 2 - 1 - (number - (row_pos - len(list_first[0]) // 2 + 1))):
            list_first[len(list_first[0]) // 2 + 1][(len(list_first[0]) // 2 - 1) - (number - (row_pos - (len(list_first[0]) // 2 + 1)))] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return (len(list_first[0]) // 2 + 1), ((len(list_first[0]) // 2 - 1) - (number - (row_pos - (len(list_first[0]) // 2 + 1))))
        elif (number - (row_pos - len(list_first[0]) // 2 + 1)) - lenght > 1 and (len(list_first[0]) // 2 + 1) - ((number - (row_pos - len(list_first[0]) // 2 + 1)) - lenght) >= len(list_first[0]) // 2 - 1:
            list_first[(len(list_first[0]) // 2 + 1) - ((number - (row_pos - len(list_first[0]) // 2 + 1)) - lenght)][1] = ['X']
            list_first[row_pos][column_pos] = ['*']
            return ((len(list_first[0]) // 2 + 1) - ((number - (row_pos - len(list_first[0]) // 2 + 1)) - lenght)), 1
    if row_pos == len(list_first[0]) // 2 + 1 and 1 <= column_pos < len(list_first[0]) // 2:
        list_first[len(list_first[0]) // 2 - 1][len(list_first[0]) // 2 - 1] = ['X']
        list_first[row_pos][column_pos] = ['*']
        return (len(list_first[0]) // 2 - 1), (len(list_first[0]) // 2 - 1)
    else:
        list_first[len(list_first[0]) // 2 - 1][len(list_first[0]) // 2] = ['X']
        list_first[row_pos][column_pos] = ['*']
        return 0, 2


# Print matrix(playground) on terminal
def tlacsachovnicu(list_first: list):
    for row in range(len(list_first)):
        for column in range(len(list_first[row])):
            print(list_first[row][column], end="")
        print()


# Generates random number which represents rolling the dice
def random_gen():
    return int(randrange(1, 7))


def main():
    size = int(input("Enter size of playground (odd number): "))
    main_list = gensachovnicu(size)
    hrac = 0
    movement = 1
    row = column = 1

    while 1:

        print("Round", movement)

        if hrac == 0:
            for i in range(3):          # Rolling 3 times to get 6 on dice
               x = random_gen()
               print("Player 1 rolled:", x)
               if x == 6:
                   print("You rolled 6, can now move with your avatar and you are rolling again")
                   hrac = 1
                   main_list[1][(size//2)+2] = ["X"]            # Set the avatar on the start position
                   x = random_gen()
                   print("You rolled:", x)                      # Rolling again
                   row, column = cal_init_move(main_list, x)
                   tlacsachovnicu(main_list)
                   break
        else:
            x = random_gen()
            print("You rolled", x)
            row, column = main_move(main_list, row, column, x)
            tlacsachovnicu(main_list)
            print()

            if row == 0:
                print("Player 1 wins!")
                break

            time.sleep(3)

        movement += 1


if __name__ == "__main__":
    main()
