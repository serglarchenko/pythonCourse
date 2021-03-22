class Company:
    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def hire_employee(self, employee):
        employee_list = list()
        if (employee.title == 'manager' or employee.title == 'engineer')
            employee_list.append(employee)
        else:
            print('We can not hire you to this position')
