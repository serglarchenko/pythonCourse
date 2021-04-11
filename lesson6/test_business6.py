import time

import pytest

from lesson6.task6_business import *


def test_add_employees(create_fruit_company, create_employee_alex, create_employee_bill):
    alex = create_employee_alex
    bill = create_employee_bill
    create_fruit_company.add_employee(alex)
    create_fruit_company.add_employee(bill)
    count_employees = len(create_fruit_company.employees)
    assert count_employees == 2, f"{count_employees} is not equal 2"


# test parallel run
@pytest.mark.smoke
@pytest.mark.parametrize('employee', [Employee('Joe', 22), Employee('Zoe', 22)])
def test_create_some_employees(employee):
    time.sleep(1)
    assert employee.age >= 18, f"employee age {employee.age} is not equal 22"


# @pytest.mark.skip
def test_fire_employee(create_fruit_company, create_employee_bill):
    fruits_company = create_fruit_company
    bill = create_employee_bill
    fruits_company.add_employee(bill)
    fruits_company.dismiss_employee(bill)
    assert bill not in fruits_company.employees, f"{bill} not in {create_fruit_company}"
    assert len(fruits_company.employees) == 0, "Employees count wrong"


@pytest.mark.smoke
def test_get_bankrupt(do_bankrupt, bankrupt_company_money):
    b = bankrupt_company_money
    d = do_bankrupt
    assert d == b, f" Bunkrupt company money {b} is not 0"


def test_show_company_money(show_money_after_creation, start_company_money):
    assert show_money_after_creation == start_company_money, f"{show_money_after_creation} is not equal " \
                                                             f"{start_company_money} "


def test_create_company(create_fruit_company):
    expected_company = Company('Fruits', address='Ocean street, 1')
    assert create_fruit_company == expected_company, f"{create_fruit_company} is not equal {expected_company}"
