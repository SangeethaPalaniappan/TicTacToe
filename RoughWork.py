n = int(input("n : "))
for i in range(n):
   print(list(range(1 + n * i, 1 + n * (i + 1))))
   matrix = [list(range(1 + n * i, 1 + n * (i + 1)))] + matrix
print(matrix)   
number = 0
init = 0
for i in range(n):
    if matrix[i][i] == number: 
        init = 1
        continue
        
    else:
        init = 0
        break
if init == 1:
    print("stop")    
for i in range(n):
    for j in range(n):
        if matrix[i][j] == number:
            init = 1
            continue
        else:
            init = 0
            break
for i in range(n):
    for j in range(n):
        if matrix[j][i] == number:
            init = 1
            continue
        else:
            init = 0
            break
j = n -1
for i in range(n):
    if matrix[i][j] == number:
        init = 1
        j -= 1
    else:
        init = 0
        break    