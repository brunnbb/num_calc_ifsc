import numpy as np
from sympy import Matrix, sympify, lambdify

def non_linear_newton_method(system, guess, tol=1e-6, max_itr=100):
    equations = [sympify(eq[0]) for eq in system]
    variables = sorted(set().union(*[eq.free_symbols for eq in equations]), key=lambda s: s.name)
    
    num_vars = len(variables)
    if num_vars != len(guess):
        raise ValueError("Number of variables in the system does not match the length of the initial guess.")
    
    F = Matrix(equations)
    J = F.jacobian(variables)
    
    F_func = lambdify(variables, F, 'numpy')  
    J_func = lambdify(variables, J, 'numpy')  

    X = np.array(guess, dtype=np.float64).reshape(-1, 1)

    for iteration in range(max_itr):
        F_val = np.array(F_func(*X.flatten()), dtype=np.float64).reshape(-1, 1)
        J_val = np.array(J_func(*X.flatten()), dtype=np.float64)

        delta_X = np.linalg.solve(J_val, -F_val)
        X += delta_X

        if np.linalg.norm(delta_X, ord=2) <= tol:
            print(f"Converged after {iteration + 1} iterations.")
            return X.flatten()

    print("Did not converge within the maximum number of iterations.")
    return X.flatten()

if __name__ == "__main__":
    system = [
        ["x**2/3 + y**2 - 1"],
        ["x**2 + y**2/4 - 1"]
    ]
    guess = [0.3, 0.2]
    solution = non_linear_newton_method(system, guess)
    print("Solution 1:", solution)
    print()
    system = [
        ["x**2 - cos(x*y) - 1"],
        ["sin(y) - 2*cos(x)"]
    ]
    guess = [1.5, 0.5]
    solution = non_linear_newton_method(system, guess)
    print("Solution 2:", solution)
    print()
    system = [
        ["pi*cos(x*y) - 2 + z"],
        ["exp(x*y-1) + x*y*z - 4"],
        ["x*y + y*z - x - y"]
    ]
    guess = [1.0, 1.0, 2.0]
    solution = non_linear_newton_method(system, guess)
    print("Solution 3:", solution)
