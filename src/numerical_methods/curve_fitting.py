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

def calc_residue(xi: np.ndarray, yi: np.ndarray, poly: callable): # type: ignore
  return sum((yi-poly(xi))**2)

if __name__ == '__main__':
    xi = np.array([0, 0.25, 0.5, 0.75, 1])
    yi = np.array([-153, 64, 242, 284, 175])
    f = curve_fit(xi, yi, function_type='1+1*x+1*x**2')
    print(f(2))
    plot_points_and_function(xi, yi, f)

