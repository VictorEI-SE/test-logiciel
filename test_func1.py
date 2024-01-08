import unittest
import func1 

class TestThreeLargestValues(unittest.TestCase):
    def test_three_largest_values_normal(self):
        result = func1.three_largest_values([1, 5, 2, 8, 3, 10])
        self.assertEqual(result, [10, 8, 5])

    def test_three_largest_values_short_list(self):
        result = func1.three_largest_values([7, 4])
        self.assertEqual(result, "La liste est trop petite")

    def test_three_largest_values_equal_values(self):
        result = func1.three_largest_values([5, 5, 5])
        self.assertEqual(result, [5, 5, 5])


'''class TestNSmallestValues(unittest.TestCase):
    def test_n_smallest_values_normal(self):
        result = func1.n_smallest_values([1, 5, 2, 8, 3, 10], 3)
        self.assertEqual(result, [1, 2, 3])

    def test_n_smallest_values_short_list(self):
        result = func1.n_smallest_values([7, 4], 3)
        self.assertEqual(result, "La liste est trop petite")

    def test_n_smallest_values_equal_values(self):
        result = func1.n_smallest_values([5, 5, 5], 2)
        self.assertEqual(result, [5, 5])

class TestIsPrime(unittest.TestCase):
    def test_is_prime_valid(self):
        self.assertTrue(func1.is_prime(2))
        self.assertTrue(func1.is_prime(7))
        self.assertFalse(func1.is_prime(4))
        self.assertFalse(func1.is_prime(1))
        self.assertTrue(func1.is_prime(17))
        self.assertFalse(func1.is_prime(25))

class TestIsArithmetic(unittest.TestCase):
    def test_is_arithmetic_normal(self):
        result = func1.is_arithmetic([2, 4, 6, 8, 10])
        self.assertTrue(result)

    def test_is_arithmetic_short_list(self):
        result = func1.is_arithmetic([7, 4])
        self.assertTrue(result)

    def test_is_arithmetic_not_arithmetic(self):
        result = func1.is_arithmetic([2, 4, 7, 8, 10])
        self.assertFalse(result)


class TestIsGeometric(unittest.TestCase):
    def test_is_geometric_normal(self):
        result = func1.is_geometric([2, 6, 18, 54, 162])
        self.assertTrue(result)

    def test_is_geometric_short_list(self):
        result = func1.is_geometric([7, 4])
        self.assertTrue(result)

    def test_is_geometric_not_geometric(self):
        result = func1.is_geometric([2, 6, 12, 54, 162])
        self.assertFalse(result)'''

if __name__ == '__main__':
    unittest.main()