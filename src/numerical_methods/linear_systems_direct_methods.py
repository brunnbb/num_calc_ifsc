import numpy as np

# Basic linear system as a matrix operation : A.x = b
# Solves x  

def gauss_elimination(A, b):
    n: int = len(A)
    for j in range(n):
        for i in range(j + 1, n):
            factor = A[i, j] / A[j, j]
            b[i] -= factor * b[j]
            A[i, j:] -= factor * A[j, j:]
    x = solve_upper_triangular(A, b)
    return A, b, x

def gauss_elimination_with_partial_pivoting(A, b):
    n: int = len(A)
    for j in range(n):
        max_row_index = np.argmax(abs(A[j:, j])) + j
        if A[max_row_index, j] == 0:
            raise ValueError("The system has no solution")
        
        if max_row_index != j:
            A[[j, max_row_index]] = A[[max_row_index, j]]
            b[[j, max_row_index]] = b[[max_row_index, j]]
            
        for i in range(j + 1, n):
            factor = A[i, j] / A[j, j]
            b[i] -= factor * b[j]
            A[i, j:] -= factor * A[j, j:]
    x = solve_upper_triangular(A, b)
    return A, b, x

def gauss_elimination_with_reduced_matrix(A, b):
    n: int = len(A)
    for j in range(n):
        if A[j, j] == 0:
            raise ValueError(f"Zero diagonal element at index {j}, system is singular or ill-conditioned.")
        
        pivot = A[j, j]
        A[j, :] /= pivot
        b[j] /= pivot
        
        for i in range(j + 1, n):
            factor = A[i, j]
            A[i, j:] -= factor * A[j, j:]
            b[i] -= factor * b[j]

    for j in range(n-1, -1, -1):
        for i in range(j - 1, -1, -1):
            factor = A[i, j]
            A[i, j:] -= factor * A[j, j:]
            b[i] -= factor * b[j]
            
    A = fix_negative_zeros(A)
    b = fix_negative_zeros(b)
    x = b
    return A, b, x    

def lu_decomposition(A, b):
    n: int = len(A)
    L = np.identity(n)
    U = np.copy(A)
    
    for j in range(n):
        for i in range(j + 1, n):
            factor = U[i, j] / U[j, j]
            L[i, j] = factor
            U[i, j:] -= factor * U[j, j:]
    y = solve_lower_triangular(L, b)
    x = solve_upper_triangular(U, y)
    return U, L, y, x

def solve_upper_triangular(U, b):
    n: int = len(U)
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        Sum = b[i]
        for j in range(i + 1, n):
            Sum -= U[i, j] * x[j]
        if U[i, i] == 0:
            raise ValueError(f"Zero diagonal element at index {i}, system is singular or ill-conditioned.")
        x[i] = Sum / U[i, i]
    return x

def solve_lower_triangular(L, b):
    n: int = len(U)
    x = np.zeros(n, dtype=float)
    for i in range(n):
        Sum = b[i]
        for j in range(i):
            Sum -= L[i, j] * x[j]
        x[i] = Sum / L[i, i]
    return x

def show_matrixes(matrix_dict: dict):
    for key, value in matrix_dict.items():
        print(f"{key}: ")
        print(value)
    
def fix_negative_zeros(matrix, threshold=1e-12):
    matrix[np.abs(matrix) < threshold] = 0
    return matrix    
    
if __name__ == "__main__":
    A = np.array([[3, -2, 1], [4, 3, -3], [-6, 4, -7]], dtype=float)
    b = np.array([5, 1, 3], dtype=float)
    U, b_mod, x = gauss_elimination(A, b)
    show_matrixes({"U": U, "b_mod": b_mod, "x": x})
    print()
    A = np.array([[3, -2, 1], [4, 3, -3], [-6, 4, -7]], dtype=float)
    b = np.array([5, 1, 3], dtype=float)
    U, b_mod, x = gauss_elimination_with_partial_pivoting(A, b)
    show_matrixes({"U": U, "b_mod": b_mod, "x": x})
    print()
    A = np.array([[3, -2, 1], [4, 3, -3], [-6, 4, -7]], dtype=float)
    b = np.array([5, 1, 3], dtype=float)
    U, b_mod, x = gauss_elimination_with_reduced_matrix(A, b)
    show_matrixes({"U": U, "b_mod": b_mod, "x": x})
    print()
    A = np.array([[3, -2, 1], [4, 3, -3], [-6, 4, -7]], dtype=float)
    b = np.array([5, 1, 3], dtype=float)
    U, L, y, x = lu_decomposition(A, b)
    show_matrixes({"U": U, "L": L, "y": y, "x": x})
