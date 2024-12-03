import numpy as np
np.set_printoptions(precision=16)

def gaussJacobi(A, b, tolerance=0, max_iter=100):
    n: int = len(b)
    x = np.zeros(n, dtype=np.float64)  
    x_new = np.zeros(n, dtype=np.float64)  
    
    for iteration in range(1, max_iter + 1):
        for i in range(n):
            sum_except_i = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_except_i) / A[i, i]
        
        print(f'Iter {iteration:03}: {x}')
        if np.linalg.norm(x_new - x, ord=np.inf) <= tolerance:
            return x_new, iteration

        x = np.copy(x_new)

    return x_new, max_iter    

def gaussSeidel(A, b, tolerance=0, max_iter=100):
    n = len(b)
    x = np.zeros(n, dtype=np.float64)  
    
    for iteration in range(1, max_iter + 1):
        x_new = np.copy(x)  
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:]) 

            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        print(f'Iter {iteration:03}: {x}')
        if np.linalg.norm(x_new - x, ord=np.inf) <= tolerance:
            return x_new, iteration
        x = x_new
    
    return x, max_iter
                   
if __name__ == "__main__":    
    A = np.array([[10, 1],[1, 8]], dtype=np.float64)
    b = np.array([23, 26], dtype=np.float64)
    print(gaussJacobi(A, b))
    print(gaussSeidel(A, b))

