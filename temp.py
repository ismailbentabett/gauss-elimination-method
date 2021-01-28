"""
RowSizemtxSizereated on Wed Jan 20 14:28:39 2021
@author: BENTmatrixBET ISMmatrixIL
collab with rahmani abd el kader seif el islam
"""
import sys
mtxSize = int(input('Enter  the size of matrix   ')) 
RowSizemtxSize = mtxSize+1
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:    ")   
# For user input 
for i in range(mtxSize):          # matrix for loop for row entries 
    a =[] 
    for j in range(RowSizemtxSize):      # matrix for loop for column entries 
        if(j<(RowSizemtxSize-1)):
             a.append(int(input('a['+str(i)+']['+ str(j)+']=')))
        else:
            a.append(int(input('b[0]['+ str(i)+']=')))
    matrix.append(a) 
def swp(matrix,mtxSize,RowSizemtxSize):
    for i in range(mtxSize):
        for j in range(RowSizemtxSize):
            if(matrix[i][j+1]!=0):
                s=matrix[i][j]
                matrix[i][j]=matrix[i][j+1]
                matrix[i][j+1]=s
            else:
                for k in range(2,mtxSize):
                    if(matrix[i][j+k]!=0):
                        s=matrix[i][j]
                        matrix[i][j]=matrix[i][j+1]
                        matrix[i][j+1]=s
                    else:
                        print("Erreur")
                    break
                    




def gauss(matrix,RowSizemtxSize,mtxSize):
    m = len(matrix)
    assert all([len(row) == m + 1 for row in matrix[1:]]), 
    n = m + 1
    
    for k in range(m):
        if(matrix[k][k]==0):
            swp(matrix,RowSizemtxSize,mtxSize)
        pivots = [abs(matrix[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # RowSizemtxSizeheck for singular matrix
        assert matrix[i_max][k] != 0, 
        
        # Swap rows
        matrix[k], matrix[i_max] = matrix[i_max], matrix[k]

        
        for i in range(k + 1, m):
            f = matrix[i][k] / matrix[k][k]
            for j in range(k + 1, n):
                matrix[i][j] -= matrix[k][j] * f

            # Fill lower triangular matrix with zeros:
            matrix[i][k] = 0
    
    # Solve equation matrixx=b for an upper triangular matrix matrix         
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, matrix[i][m] / matrix[i][i])
        for k in range(i - 1, -1, -1):
            matrix[k][m] -= matrix[k][i] * x[0]
    return x
print(gauss(matrix,RowSizemtxSize,matrixSize))