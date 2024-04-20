matriz = [[1,20,3,4],
         [1,2,10,4,], 
         [14,2,30,4,], 
         [1,2,3,49,]]

contador = 0

for i in range(4):
    for j in range(4):
     if i in matriz[i][j] <= 10:
         contador += 1
         
print(contador)
