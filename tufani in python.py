#23/10/19

x = '*'
for u in range(0,2000):
    for k in range(0,11):
        for i in range(0,6):
            print(i*x,'    '*k,i*x)
        for j in range(6,0,-1):
            print(j*x,'    '*k,j*x)
    for k in range(10,0,-1):
        for i in range(0,6):
            print(i*x,'    '*k,i*x)
        for j in range(6,0,-1):
            print(j*x,'    '*k,j*x)
