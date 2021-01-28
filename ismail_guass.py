
import sys
matrixSize = int(input('Enter  the size of matrix   : ')) 
RowSize = matrixSize+1
matrix = [] 
print("Enter the entries row size  :   ")   
for i in range(matrixSize):        
    a =[] 
    for j in range(RowSize):       
        if(j<(RowSize-1)):
             a.append(int(input('matrix['+str(i)+']['+ str(j)+']=')))
        else:
            a.append(int(input('b[0]['+ str(i)+']=')))
    matrix.append(a) 
def swp(matrix,matrixSize,RowSize):
    for i in range(matrixSize):
        for j in range(RowSize):
            if(matrix[i][j+1]!=0):
                s=matrix[i][j]
                matrix[i][j]=matrix[i][j+1]
                matrix[i][j+1]=s
            else:
                for k in range(2,matrixSize):
                    if(matrix[i][j+k]!=0):
                        s=matrix[i][j]
                        matrix[i][j]=matrix[i][j+1]
                        matrix[i][j+1]=s
                    else:
                        print("Erreur")
                    break
                    




def gauss(matrix,RowSize,matrixSize):
    m = len(matrix)
    assert all([len(row) == m + 1 for row in matrix[1:]]) 
    n = m + 1
    
    for k in range(m):
        if(matrix[k][k]==0):
            swp(matrix,RowSize,matrixSize)
        pivots = [abs(matrix[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # RowSizeheck for singular matrix
        assert matrix[i_max][k] != 0
        
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
print(gauss(matrix,RowSize,matrixSize))