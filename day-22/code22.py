m = int(input("Enter first number above 1: "))
n = int(input("Enter second number: "))

thisDict = {}
if m > 1 and n > m:                         # to check if nums are positive
    for i in range(m, n+1):
        j = i
        a = 0                               # initializing count for each number
        while j != 1:
            if j % 2 == 1:                  # collartz function
                j = 3*j + 1
            else:
                j = j/2
            a += 1
        thisDict[i] = a                     # setting values to dictionary
max_num = max(zip(thisDict.values(), thisDict.keys()))[1]
print("The number with the highest no. of steps: ", max_num)