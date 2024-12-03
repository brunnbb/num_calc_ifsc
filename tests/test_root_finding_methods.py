import unittest
from src.numerical_methods.root_finding_methods import bisection_method, fixed_point_method, babilonic_method, newton_method, secant_method

class TestRootFindingMethods(unittest.TestCase):
    def test_newton_method(self):
        self.assertEqual(newton_method("x**3-3*x+1", 2, iterations=5), 1.532088886237968)
        self.assertAlmostEqual(newton_method("x**2 - 2", 2, iterations=10), 1.4142135623730951)
        self.assertEqual(newton_method("x**2-9", 3.2), 3 )
        self.assertEqual(newton_method("x**2-9", 2.8), 3 )
        self.assertEqual(newton_method("x**2-9", -3.1), -3 )
        self.assertEqual(newton_method("x**2-9", 0.1), 3 )

if __name__ == "__main__":
    unittest.main()