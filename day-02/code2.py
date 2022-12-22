lst = []
d = 0               #dynamic
n = int(input("No. of Triangles: " ))

if n>0:
    for i in range(0,n):            
        d = d+1
        a, b, c= [int(item) for item in input(f'Triangle {d} sides: ').split()]
        k = a, b, c
        lst.append(k)

    for x in range(0,n):
        a, b, c = lst[x]
        if x%3==0:          
            if a<b and a<c:
                print(a)
            elif b<a and b<c:
                print(b) 
            else:   
                print(c)
        elif x%3==1:            
            if ((a<b and b<c) or (c<b and b<a)):
                print(b)
            elif ((b<a and a<c) or (c<a and a<b)):
                print(a)
            else:  
                print(c)
        else:           
            if a>b and a>c:
                print(a)
            elif b>a and b>c:
                print(b)
            else:
                print(c)  