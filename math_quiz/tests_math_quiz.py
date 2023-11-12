import unittest
from math_quiz import values, operation, result


class TestMathGame(unittest.TestCase):

    def test_values(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = values(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation(self):
        # Test if the random operation is one of the expected operators
        for i in range(1000):  # Test a large number of random values
            rand_op = operation()
            self.assertIn(rand_op, ['+', '-', '*'])

    def test_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 6, '*', '4 * 6', 24),
                (2, 7, '-', '2 - 7', -5)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
