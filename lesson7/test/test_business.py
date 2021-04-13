import unittest
from lesson7.business import *
from lesson7.resourse.constants import *


class TestBusinessModel(unittest.TestCase):

    def test_creation_company(self):
        fruits_company = Company('Fruits', address='Ocean street, 1')
        self.assertEqual(fruits_company, Company('Fruits', address='Ocean street, 1'), f'Expected company name - '
                                                                                       f'{fruits_company.name} is not equal actual company name {FRUIT_COMPANY}')

    def test_hash_code_alex(self):
        alex = Alex('Aleks', 22).__hash__()
        alex1 = Alex('Aleks', 23).__hash__()
        self.assertTrue(alex == alex1, f'Hash code alex {alex} is not equal {alex1}')

    def test_alex_is_engineer(self):
        alex = Alex('Aleks', 22)
        self.assertTrue(isinstance(alex, Engineer), f'Person {alex.name} is not instance of {Engineer}')


if __name__ == '__main__':
    unittest.main()
