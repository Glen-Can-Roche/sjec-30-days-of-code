# input n
n = int(input("Enter the width of diamond: "))
n = n-1
for i in range(n):     # top part
    for j in range(n - i):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        print(end=" #")
    # for new line
    print()
for i in range(n, -1, -1):     # lower part
    for j in range(n - i):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        print(end=" #")
    # for new line
    print()