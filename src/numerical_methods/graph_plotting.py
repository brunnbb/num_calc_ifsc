import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Basic, lambdify

x, y, z = symbols('x y z')

def plot_function(expr, interval : tuple):
    
    #Creates a numeric expression
    f = lambdify(x, expr, 'numpy')
    
    #Creates x values for the interval
    x_vals = np.linspace(interval[0], interval[1])
    
    #Creates y values and plots them
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label=f'y = {expr}')
    
    # (0,0) Axis
    plt.axhline(0, color='black',linewidth=2)
    plt.axvline(0, color='black',linewidth=2)  
    
    #Subtitles and details
    plt.title(f'Function: {expr}')
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('y', fontsize=12, fontweight='bold')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def plot_tan_function(expr, interval : tuple):
    f = lambdify(x, expr, 'numpy')

    x_vals = np.linspace(interval[0], interval[1], 1000)

    y_vals = f(x_vals)

    y_vals = np.where(np.abs(y_vals) > 1, np.nan, y_vals)

    plt.plot(x_vals, y_vals, label=f'y = {expr}')

    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)

    plt.title(f'Function: {expr}')
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('y', fontsize=12, fontweight='bold')
    plt.legend()
    plt.grid(True)
    plt.ylim([-1, 1])
    plt.show()

def plot_points_and_function(xi: np.ndarray, yi: np.ndarray, poly: callable): # type: ignore
    x_vals = np.linspace(min(xi) - 1, max(xi) + 1, 500)
    y_vals = poly(x_vals)
    
    plt.plot(x_vals, y_vals, label="Polynomial function", color='blue')
    plt.scatter(xi, yi, color='red', label="Data Points", zorder=5)
    
    plt.axhline(0, color='black', linewidth=2)  
    plt.axvline(0, color='black', linewidth=2) 
    
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()