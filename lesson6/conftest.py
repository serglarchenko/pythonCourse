import pytest

from lesson6.business_6 import *


@pytest.fixture(scope="function")
def create_fruit_company():
    return Company('Fruits', address='Ocean street, 1')


@pytest.fixture()
def create_employee_bill():
    return Engineer('Bill', 20)


@pytest.fixture()
def create_employee_alex():
    return Engineer('Alex', 30)


@pytest.fixture()
def create_employee_jane():
    return Engineer('Jane', 40)


@pytest.fixture()
def do_bankrupt():
    company = Company('Fruits', address='Ocean street, 1')
    company.go_bankrupt()
