import time
import turtle

print(time.time()//1440)
print(50*365)


try:
    f = open('teest.txt')
    if f.name != 'test.txt':
        raise Exception
except FileNotFoundError as q:           #FileNotFoundError: default python dlhá správa
    print(q)
except Exception as e:
    print("Mnou vytvorená Exception")
else:
    print(f.read())
    f.close
finally:                    # Urobí sa vždy, nehladiac na predošlé veci
    print("Toto sa aj tak vypíše!")


def simple_raise(num,n):
    sum = 1
    for i in range(n):
        sum = sum*num
    print(sum)

def raise_n(a,b,c,n):
    simple_raise(a,n)
    simple_raise(b,n)
    simple_raise(c,n)


def is_triagle(a, b, c):
    out_p = "Can not form triangle."
    if a+b < c or a+c < b or b+c < a:
        print(out_p)
    else:
        print("Triangle can be formed.")


def video(feet = 0, inches = 0):            # keyword arguments
    inputt = input("Enter code:")
    if len(inputt) < 6:                     # funkcia "len()"
        print("Your string is less than 6 letters.")
    else:
        print("Your string is more than 6 letters.")


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)

is_triagle(2,3,8)

raise_n(5,4,3,2)

turtle.exitonclick()
