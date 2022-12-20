print("Enter two non-negative numbers: ")
a = int(input('num 1: '))
b = int(input('num 2: '))
c = b+1

if a > 0 and b > 0:
    for n in range(a,c):
        if n%3==0:
            print("Foo")
        elif n%2==0 and n%3!=0:
            print("Bar")
        elif n%2!=0 and n%3!=0:
            print("Baz")
        else:
            break