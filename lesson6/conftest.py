import os
import time

import pytest

from lesson6 import constants
from lesson6.task6_business import *


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    start_time = time.time()
    outcome = yield
    rep = outcome.get_result()
    end_time = time.time()
    execution_time = end_time - start_time
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures.txt") else "w"
        with open("failures.txt", mode) as f:
            f.write(f"{rep.nodeid} - execution time: {execution_time} \n")

    if rep.when == "call" and rep.passed:
        mode = "a" if os.path.exists("passed.txt") else "w"
        with open("passed.txt", mode) as f:
            f.write(f"{rep.nodeid} - execution time: {execution_time} \n")


@pytest.fixture(scope='function')
def get_test_name(request):
    print(request.node.name + 'starts!')

    def get_test_name_finish():
        print(request.node.name + 'finished!')

    request.addfinalizer(get_test_name_finish)
    return request.fixturename


@pytest.hookimpl
@pytest.fixture
def create_fruit_company() -> Company:
    return Company('Fruits', address='Ocean street, 1')


@pytest.fixture()
def create_employee_bill() -> Engineer:
    return Engineer('Bill', 20)


@pytest.fixture()
def create_employee_alex():
    return Engineer('Alex', 30)


@pytest.fixture()
def create_employee_jane():
    return Engineer('Jane', 40)


@pytest.fixture()
def bankrupt_company_money():
    return constants.NO_MONEY


@pytest.fixture()
def start_company_money():
    return constants.MONEY_AFTER_CREATION_COMPANY


@pytest.fixture
def show_money_after_creation(create_fruit_company):
    return create_fruit_company.show_money()


@pytest.fixture()
def do_bankrupt(create_fruit_company):
    company = create_fruit_company
    company.go_bankrupt()
    return company.show_money()
