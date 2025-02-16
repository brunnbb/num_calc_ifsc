import numpy as np
import sympy as sp
from graph_plotting import plot_points_and_function

x = sp.symbols('x')

def curve_fit(xi, yi, function_type: str = '1 + 1*x'):
    function = sp.sympify(function_type, locals={'x': x})
    terms = function.as_ordered_terms()  
    print(terms)

    # Replace constants with 1 and extract basis functions
    basis_functions = []
    for term in terms:
        coeff = term.coeff(x, right=True)  # Avoids division by zero
        term = term / coeff if coeff != 0 else term  # Normalize terms
        basis_functions.append(sp.lambdify(x, term, 'numpy'))

    V = np.array([[f(xi_val) for f in basis_functions] for xi_val in xi])

    coeffs = np.linalg.inv(V.T @ V) @ V.T @ yi
    fitted_function = sum(c * term for c, term in zip(coeffs, terms))
    print(f"Fitted function: f(x) = {(fitted_function)}")

    return sp.lambdify(x, fitted_function, 'numpy')

if __name__ == '__main__':
    xi = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    yi = np.array([31, 35, 37, 33, 28, 20, 16, 15, 18, 23, 31])
    f = curve_fit(xi, yi, function_type='1+sin(2*pi*x)+cos(2*pi*x)')
    plot_points_and_function(xi, yi, f)

