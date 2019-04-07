import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('James', 'Smith', '10000')

    def test_give_default_raise(self):
        new_salary = self.employee.salary + 5000
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, new_salary)

    def test_give_custom_raise(self):
        custom_salary = 250
        new_salary = self.employee.salary + custom_salary
        self.employee.give_raise(custom_salary)
        self.assertEqual(self.employee.salary, new_salary)


if __name__ == '__main__':
    unittest.main()
