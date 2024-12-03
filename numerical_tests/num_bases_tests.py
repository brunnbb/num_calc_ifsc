import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from numerical_methods.root_finding_methods import *
from numerical_methods.graph_plotting import *

if __name__ == "__main__":
    print("\nBisseção:")
    func_expr = "sin(3*x+8)"
    print(f"R: {bisection_method(func_expr, 1, 2, 10, 1e-2)}")
    
    print("\nNewton:")
    print(
        f"R: {newton_method(expr = func_expr, xi = 1.5, iterations = 10, precision = 1e-8):.7f}\n"
    )
