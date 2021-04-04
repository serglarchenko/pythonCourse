from lesson6.business_6 import *

fruits_company = Company('Fruits', address='Ocean street, 1')
alex = Engineer('Alex', 55)
bill = Engineer('Bill', 20)
jane = Manager('Jane', 30)


def test_show_company_money():
    money = fruits_company.show_money()
    assert (money, 1000)


def test_add_employees():
    fruits_company.add_employee(alex)
    fruits_company.add_employee(bill)
    assert (len(fruits_company.employees), 2)


def test_fire_employee():
    fruits_company.dismiss_employee(bill)
    assert (bill not in fruits_company.employees, True)
    assert (len(fruits_company.employees), 1)
