"""
Created on Wed Jan 20 14:28:39 2021
@author: BENTABET ISMAIL
collab with rahmani abd el kader seif el islam
"""
import sys
R = int(input('Enter  the size of matrix   ')) 
C = R+1
# Initialize matrix 
A = [] 
print("Enter the entries rowwise:    ")   
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
        if(j<(C-1)):
             a.append(int(input('a['+str(i)+']['+ str(j)+']=')))
        else:
            a.append(int(input('b[0]['+ str(i)+']=')))
    A.append(a) 
def swp(A,R,C):
    for i in range(R):
        for j in range(C):
            if(A[i][j+1]!=0):
                s=A[i][j]
                A[i][j]=A[i][j+1]
                A[i][j+1]=s
            else:
                for k in range(2,R):
                    if(A[i][j+k]!=0):
                        s=A[i][j]
                        A[i][j]=A[i][j+1]
                        A[i][j+1]=s
                    else:
                        print("Erreur")
                    break
                    




def gauss(A,C,R):
    m = len(A)
    assert all([len(row) == m + 1 for row in A[1:]]), 
    n = m + 1
    
    for k in range(m):
        if(A[k][k]==0):
            swp(A,C,R)
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # Check for singular matrix
        assert A[i_max][k] != 0, 
        
        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]

        
        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0
    
    # Solve equation Ax=b for an upper triangular matrix A         
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x
print(gauss(A,C,R))