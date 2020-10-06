
def grid(n):

        for k in range(1,n+1):          # robi pod seba
             for i in range(1,3*n):         # robi riadky
                 for q in range(1,n+1):         # robi vedla seba
                    for j in range(1,3*n):              # robi sltpce
                        if(((i==1) and (j==1)) or ((3*n-1==q*3-1==j) and (i==1)) or (k==3 and i==3*n-1 and (j==1 or j==3*n-1==q*3-1))):
                             print("+", end = " ")
                        elif(i==1 and j!=1 or (k==3 and i==3*n-1 and j!=1)):
                              print("-", end = " ")                     
                        elif(j==1 or 3*n-1==3*q-1==j):
                              print(" |  ", end = " ")
                        else:
                            print(" ", end = " ")
                 print()
                    

# grid(3)                     # volanie funkcie

def gold(n):

        for i in range(1,n*3+1):
            for q  in range(1,n+1):
                for j in range(1,n*3+1):
                    if(i==j==1):
                        print("o", end = " ")
                    elif(i==1 or j==1):
                        print("a", end = " ")
                    else:
                        print("c", end = " ")
            print()





gold(3)
