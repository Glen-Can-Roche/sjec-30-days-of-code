a, b = input("Enter the row and column: ").split()
a = int(a)
b = int(b)
c = a*b
print("Does L shape cover all the squares:\t")
if(c%6==0):
    print("Yes")
else:
    print("No")