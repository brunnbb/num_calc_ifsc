import sympy as sp
import numpy as np
from graph_plotting import plot_points_and_function

x = sp.symbols('x')

def lagrange_interpolation(xi: np.ndarray, yi: np.ndarray):
    n = len(xi)
    expr = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if j != i:
                l *= (x - xi[j]) / (xi[i] - xi[j])
        print(f'L{i}: {sp.expand(l)}')
        expr += yi[i] * l
    print(f'Lagrange polynomial: {sp.simplify(expr)}')
    return sp.lambdify(x, expr, 'numpy')

if __name__ == '__main__':
    xi = np.array([-3, -2, -1, 0, 1]) 
    yi = np.array([-7, -11, -3, -1, 1])  

    lagrange_poly = lagrange_interpolation(xi, yi)
    print(f'Value at x = 3: {lagrange_poly(3)}')
    
    plot_points_and_function(xi, yi, lagrange_poly)
