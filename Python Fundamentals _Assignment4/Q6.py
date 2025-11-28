from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Calculate salary for Intern")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Calculate salary for Full Time Employee")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Calculate salary for Contractual Employee")

intern = Intern()
intern.calculate_salary()

full_time_employee = FullTimeEmployee()
full_time_employee.calculate_salary()

contract_employee = ContractEmployee()
contract_employee.calculate_salary()