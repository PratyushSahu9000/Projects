import numpy as np

#---Functions for Calculations---

def Matrix_input(rows , cols, name):
    print(f"Enter elements of matrix {name} : ")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1} : ").split()))
        if len(row)!=cols:
            raise ValueError(f"Expected {cols} elements per rows!")
        matrix.append(row)
    return np.array(matrix)
    
def add(A,B):
    return A+B

def sub(A,B):
    return A-B

def multiply(A,B):
    if A.shape[1]==B.shape[0]:
        return np.dot(A,B)
    else:
        return "Multiplication not possiblle (Dimensions Mismatch)"

def transpose(A):
    return A.T

def determinant(A):
    if A.shape[1]!=A.shape[0]:
        return "Determinant not defined for non-square matrices!"
    else:
        return np.linalg.det(A)
    
def inverse(A):    
    if A.shape[0]!=A.shape[1]:
        return "Inverse not defined for non-square matrices!"
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Inverse not possible (determinant=0)!"
    

#---Main---

while True:
    print("\n--- MENU ---")
    print("1. Addition (A + B)")
    print("2. Subtraction (A - B)")
    print("3. Multiplication (A × B)")
    print("4. Transpose (A)")
    print("5. Determinant (A)")
    print("6. Inverse (A)")
    print("7. Exit")

    choice = int(input("Enter your choice : "))

    if choice in [1,2,3]:
        rows = int(input("Enter number of rows : "))
        cols = int(input("Enter number of cols : "))
        print("Matrix A : ")
        A = Matrix_input(rows,cols, "A")
        print("Matrix B : ")
        B = Matrix_input(rows,cols,"B")

        if choice==1:
            print("\nAddition :\n" , add(A,B))
        elif choice==2:
            print("\nSubtraction :\n" , sub(A,B))
        elif choice==3:
            print("\nMultiplition :\n" , multiply(A,B))

    elif choice in [4,5,6]:
        rows = int(input("Enter number of rows : "))
        cols = int(input("Enter number of cols : "))
        print("Matrix A : ")
        A = Matrix_input(rows,cols,"A")

        if choice==4:
            print("\nTranspose :\n", transpose(A))
        elif choice==5:
            print("\nDeterminant :\n", determinant(A))
        elif choice==6:
            print("\Inverse\n", inverse(A))

    elif choice==7:
        print("---Exiting Program---")        
        print("---Thank You For Using Matrix Calculator---")
        break
    else:
        print("Invalid Choice!!!")        