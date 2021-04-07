import time

import pytest

from lesson6.business_6 import *

fruits_company = Company('Fruits', address='Ocean street, 1')
alex = Engineer('Alex', 55)
bill = Engineer('Bill', 20)
jane = Manager('Jane', 30)


@pytest.mark.show_money
def test_show_company_money():
    money = create_company().show_money()
    assert (money, 1000)


@pytest.mark.usefixtures()
def test_add_employees(create_fruit_company, create_employee_alex, create_employee_bill):
    alex = create_employee_alex
    bill = create_employee_bill
    create_fruit_company.add_employee(alex)
    create_fruit_company.add_employee(bill)
    assert (len(create_fruit_company.employees), 2)


@pytest.mark.skip
def test_fire_employee():
    fruits_company.dismiss_employee(bill)
    assert (bill not in fruits_company.employees, True)
    assert (len(fruits_company.employees), 1)


pytestmark = pytest.mark.usefixtures('do_bankrupt')


@pytest.mark.usefixtures()
def test_get_bankrupt(create_fruit_company):
    money = create_fruit_company.show_money()
    assert (money, 0)


# test parallel run
@pytest.mark.parametrize('employee', [Employee('Joe', 22), Employee('Zoe', 22)])
def test_create_some_employees(employee):
    time.sleep(1)
    assert employee.age == 22


@pytest.hookimpl(tryfirst=True)
@pytest.mark.usefixtures()
def create_company():
    return Company('Fruits', address='Ocean street, 1')
