from sympy import symbols, lambdify, diff

# This module contains methods for algebric solutions

# expr : algebric expression as a str that will be interpreted by sympy
# lambdify is used because sympy "subs" method is unbelievably slow

#For sympy to recognise these symbols as symbolic algebric variables
x = symbols('x')

def bisection_method(expr: str, a: float, b: float, iterations=100, tolerance=0.0) -> float:
    f = lambdify(x, expr, "numpy")
    root = 0

    if f(a) * f(b) > 0:
        raise ValueError("There is no root in this interval")

    for i in range(iterations + 1):
        root: float = (a + b) / 2
        f_root = f(root)

        print(f"Iteration {i}: x = {root}   Tol: {abs(a - b) / 2}")

        if abs(a - b) / 2 < tolerance or abs(f_root) < tolerance:

            print(f"The root is approximately {root} after {i} iterations.")
            return root

        if f(a) * f_root < 0:
            b = root
        else:
            a = root

    print(
        f"Max number of iterations reached. The root is approximately {root}, after {iterations} iterations."
    )
    return root

def fixed_point_method(expr: str, xi: float, iterations=100, tolerance=0.0) -> float:
    f = lambdify(x, expr, "numpy")

    for i in range(iterations):
        x_new = f(xi)
        print(f"Iteration {i}: x = {x_new} error = {abs(x_new - xi)}")

        if abs(x_new - xi) < tolerance:
            print(f"Convergence reached after {i} iterations.")
            return x_new

        xi = x_new

    print(f"Max iterations reached, last approximation is: {xi}")
    return xi

def babilonic_method(target: float, guess: float, iterations=100, tolerance=0.0) -> float:
    new_guess = 0
    for i in range(iterations):
        new_guess = (guess + target / guess) / 2
        if abs(new_guess - guess) < tolerance:
            print(f"Converged after {i + 1} iterations.")
            return new_guess
        guess = new_guess

    print(f"Max iterations reached, last approximation is: {new_guess}")
    return new_guess

def newton_method(expr: str, xi: float, iterations=100, tolerance=0.0) -> float:
    derivative_expr = diff(expr, x)
    
    f = lambdify(x, expr, "numpy")
    f_prime = lambdify(x, derivative_expr, "numpy")

    for i in range(iterations):
        xi_new = xi - f(xi) / f_prime(xi)

        if abs(xi_new - xi) < tolerance:
            print(f"Convergence tolerance reached {tolerance} at x{i} = {xi_new}")
            break

        xi = xi_new
        print(f"Iteration {i}: x = {xi}")

    return xi

def secant_method(expr: str, x1: float, x2: float, iterations=100, tolerance=0.0) -> float:
    f = lambdify(x, expr, "numpy")

    for i in range(iterations):
        denominator = f(x2) - f(x1)

        # To avoid a division by 0
        if abs(denominator) < 1e-12:
            print(f"Warning: Denominator too small at iteration {i}")
            break

        xi_new = x2 - f(x2) * (x2 - x1) / denominator

        if abs(xi_new - x2) < tolerance:
            print(f"Convergence tolerance reached {tolerance} at x{i} = {xi_new}")
            break

        print(f"Iteration {i}: x = {xi_new}")
        x1, x2 = x2, xi_new

    return x2
