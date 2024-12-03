from numerical_methods.root_finding_methods import *

func_expr = "cos(log(x-2))"

print("\nBisseção:")
print(f"R: {bisection_method(func_expr, 2.1, 2.3, tolerance=1e-8)}")
print("\nPonto Fixo")
print(f"R: {fixed_point_method("x - 0.05*cos(log(x-2))", 2.2,  tolerance=1e-8)}")
print("\nNewthon-Raphson")
print(f"R: {newton_method(func_expr, 2.2, iterations=5)}")
print("\nMétodo das secantes")
print(f"R: {secant_method(func_expr, 2.1, 2.3)}")

