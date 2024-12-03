import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from numerical_methods.root_finding_methods import *
from numerical_methods.graph_plotting import *

if __name__ == "__main__":
    print("----------------------------------------------------")
    print("Método da bisseção")
    print("----------------------------------------------------")

    print("\nQuestion 1:")
    func_expr = "x**0.5 - cos(x)"
    print(f"R: {bisection_method(func_expr, 0, 1, 3, 1e-4)}")

    print("\nQuestion 2:")
    func_expr = "x**4 - 2 * (x**3) - 4 * (x**2) + 4 * x + 4"
    print(f"{bisection_method(func_expr, -2, -1, 20, 1e-3):.7f}")

    print("\nQuestion 3 a):")
    func_expr = "2 * x * cos(2 * x) - (x + 1) ** 2"
    print(f"{bisection_method(func_expr, -3, -2, 20, 1e-5):.7f}")

    print("\nQuestion 3 b):")
    func_expr = "x * cos(x) - 2 * (x**2) + 3 * x - 1"
    print(f"{bisection_method(func_expr, 0.2, 0.3, 20, 1e-5):.6f}")

    print("\n----------------------------------------------------")
    print("Interação de ponto fixo")
    print("----------------------------------------------------")

    print("\nQuestion 1:")
    func_expr = "exp(x) - 2"
    print(
        f"R: {fixed_point_method(expr=func_expr,xi= -1.8,iterations= 30,tolerance=1e-8):.7f}"
    )

    print("\nQuestion 2 a):")
    print(f"R: {babilonic_method(119, 11, 5, 1e-6):.6f}")
    print("\nQuestion 2 b):")
    print(f"R: {babilonic_method(1020, 32, 5, 1e-6):.6f}")
    print("\nQuestion 2 c):")
    print(f"R: {babilonic_method(919, 30, 5, 1e-6):.6f}")

    print("\n----------------------------------------------------")
    print("Newton's method:")
    print("----------------------------------------------------")

    print("\nQuestion 1:")
    func_expr = "tan(x) - 2 * x**2"
    print(
        f"R: {newton_method(expr = func_expr, xi = 0.5, iterations = 10, tolerance = 1e-8):.7f}\n"
    )
    print(
        f"R: {newton_method(expr = func_expr, xi = 1.5, iterations = 10, tolerance = 1e-8):.7f}"
    )
    plot_tan_function(func_expr, (0, 2))

    print("\nQuestion 2:")
    func_expr = "cos(10 * x) - exp(-x)"
    print(
        f"R: {newton_method(expr = func_expr, xi = 0.1, iterations = 20, tolerance = 1e-8):.7f}"
    )
    print(
        f"R: {newton_method(expr = func_expr, xi = 0.5, iterations = 20, tolerance = 1e-8):.7f}"
    )
    print(
        f"R: {newton_method(expr = func_expr, xi = 0.7, iterations = 20, tolerance = 1e-8):.7f}"
    )
    print(
        f"R: {newton_method(expr = func_expr, xi = 1, iterations = 20, tolerance = 1e-8):.7f}"
    )
    print(
        f"R: {newton_method(expr = func_expr, xi = 1.3, iterations = 20, tolerance = 1e-8):.7f}"
    )
    plot_function(func_expr, (0, 5))

    print("\n----------------------------------------------------")
    print("Secant's method:")
    print("----------------------------------------------------")

    print("\nQuestion 1:")

    print(
        f"R: {secant_method(expr = "exp(-x ** 2) - x", x1 = 0.6, x2 = 0.7, iterations = 15, tolerance = 1e-10):.10f}\n"
    )
    plot_function(expr=np.e ** (-(x**2)) - x, interval=(0, 1))
