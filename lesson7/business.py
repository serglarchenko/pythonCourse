import abc

# Implement all methods where `NotImplementedError` is raised
import time
from abc import ABC


def timeit(threshold=None):
    import time
    from functools import wraps

    def outer(func):

        @wraps(func)
        def func_wrapper(*args, **kwargs):
            name = func.__name__
            start_time = time.time()
            func(*args, **kwargs)
            execution_time = time.time() - start_time
            if threshold is None:
                print(f'Executed time - {execution_time} - No threshold  - callable function is {name}')
            if threshold is not None and threshold < execution_time:
                print(f'Executed time - {execution_time} - callable function is {name}')

        return func_wrapper

    return outer


class Company(object):
    """ Represents a company """

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def __eq__(self, other):
        if isinstance(other, Company):
            return self.name == other.name and self.address == other.address
        return False

    @timeit(2)
    def add_employee(self, employee):
        # make sure employee is an instance of Engineer or Manager
        # make sure he is not employed already
        if (isinstance(employee, Engineer) or isinstance(employee, Manager)) and employee.is_employed is False:
            return self.employees.append(employee)

    @timeit(0.5)
    def dismiss_employee(self, employee):
        """
        Dismisses an employee. Employee must be a company member.
        Company should notify employee that he/she was dismissed
        """
        if employee.is_employed and employee.company.name == self.name:
            print("You are fired")
            self.employees.remove(employee)
            employee.company = None

    def notify_im_leaving(self, employee):
        """ En employee should call this method when leaving a company """
        print(f"I am {employee.name} is going to leave {self.name}")

    @timeit(0.3)
    def do_tasks(self, employee):
        """
        Engineer should call this method when he is working.
        Company should withdraw 10 money from a personal account and return
        them to engineer. That will be a payment
        :rtype: int
        """
        # make sure engineer is employed to this company
        # check employee is Engineer
        time.sleep(1)
        if employee.is_employed and isinstance(employee, Engineer):
            self.__money = self.__money - 10
            print('Task done')
            return employee.put_money_into_my_wallet(10)

    @timeit()
    def write_reports(self, employee):
        """
        Manager should call this method when he is working.
        Company should withdraw 12 money from a personal account and return
        them to manager. That will be a payment
        :rtype: int
        """
        # make sure manager is employed to this company
        # check employee is Manager
        if employee.is_employed and isinstance(employee, Manager):
            self.__money = self.__money - 12
            print('Report done!')
            return employee.put_money_into_my_wallet(12)

    def make_a_party(self):
        """ Party time! All employees get 5 money """
        # make sure a company is not a bankrupt before and after the party
        # call employee.bonus_to_salary()
        if self.is_bankrupt is not True:
            for employee in self.employees:
                employee.bonus_to_salary(self)
        else:
            print('Company is bankrupt')

    def show_money(self):
        """ Displays amount of money that company has """
        return print(self.__money)

    def go_bankrupt(self):
        """
        Declare bankruptcy. Company money are drop to 0.
        All employees become unemployed.
        """
        self.__money = 0
        for employee in self.employees:
            self.dismiss_employee(employee)

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name


class Person(object):
    """ Represents any person """

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        # make sure that this person is not employed already
        if self.is_employed is False:
            company.add_employee(self)
            self.company = company
            print(f"You already work on {company}")
        else:
            print("You can`t join to another company ")

    def become_unemployed(self):
        """ Leave current company """
        if self.is_employed is True:
            self.notify_dismissed()
            self.company.dismiss_employee(self)
            self.company = None

    def notify_dismissed(self):
        """ Company should call this method when dismissing an employee """
        print(f'You are fired from our {self.company}')

    def bonus_to_salary(self, company, reward=5):
        """
        Company should call this method on each employee when having a party
        """
        # make sure person is employed to same company
        # money + 5
        if company.name == self.company.name:
            self.put_money_into_my_wallet(reward)
            self.__money = self.__money - reward

    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    # @is_employed.setter
    # def is_employed(self, value):
    #     self.company = value

    def put_money_into_my_wallet(self, amount):
        """ Adds the indicated amount of money to persons budget """
        # Engineer and Manager will have to use this method to store their
        # salary, because __money is a private attribute
        self.__money = self.__money + amount
        return self.__money

    def show_money(self):
        """ Shows how much money person has earned """
        return print(self.__money)

    @abc.abstractmethod
    def do_work(self):
        """ This method requires re-implementation """
        self.company.do_tasks()

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'


class Engineer(Employee):

    def do_work(self):
        self.company.do_tasks(self)


# implement me


class Manager(Employee):

    def do_work(self):
        self.company.write_reports(self)


class Alex(Engineer):
    def __new__(cls, name, age, sex=None, address=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Alex, cls).__new__(cls)
        return cls.instance


def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Alex('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()

    # add second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()
