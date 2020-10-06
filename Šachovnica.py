#       sachovnica

n = int(input("Enter int value: "))

for all in range(n):
    for i in range(n):
        print("+ - - - - ", end=" ")
    print("+")

    for g in range(4):
        for j in range(n):
            print("|         ", end=" ")
        print("|")

for i in range(n):
    print("+ - - - - ", end=" ")
print("+")
