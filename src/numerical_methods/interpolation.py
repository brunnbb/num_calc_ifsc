import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

def lagrange_interpolation(values: list[tuple]):
    n: int = len(values)
    expr = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if j != i:
                l *= (x - values[j][0])/(values[i][0]-values[j][0])
        print(f'L{i}: {sp.simplify(l)}')
        expr += values[i][1]*l
    print(f'Lagrange polynomial: {sp.simplify(expr)}')
    return sp.lambdify(x, expr, 'numpy')

def plot_lagrange_interpolation(values: list[tuple], lagrange_poly: callable): # type: ignore
    x_vals = np.linspace(min([v[0] for v in values]) - 1, max([v[0] for v in values]) + 1, 500)
    y_vals = lagrange_poly(x_vals)
    
    x_points = [v[0] for v in values]
    y_points = [v[1] for v in values]
    
    plt.plot(x_vals, y_vals, label="Lagrange Polynomial", color='blue')
    plt.scatter(x_points, y_points, color='red', label="Data Points", zorder=5)
    
    plt.axhline(0, color='black',linewidth=2)  
    plt.axvline(0, color='black',linewidth=2) 
    
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Lagrange Interpolation Polynomial')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    data_points: list[tuple[int, int]] = [(-3,-7),(-2,-11),(-1,-3),(0,-1),(1,1)]
    lagrange_poly  = lagrange_interpolation(data_points)
    #print(f'Value at x = 3: {lagrange_poly(3)}')
    plot_lagrange_interpolation(data_points, lagrange_poly)