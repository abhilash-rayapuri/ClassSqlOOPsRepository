from abc import ABC, abstractmethod

# Abstract Base Class for Department Repository
class EmpRepository(ABC):
    @abstractmethod
    def insert_employee(self, Employees):
        pass
    @abstractmethod
    def update_employee(self, Employees):
        pass
    @abstractmethod
    def delete_employee(self, emp_id):
        pass
    @abstractmethod
    def get_all_employees(self, Employees):
        pass
    @abstractmethod
    def get_employee_by_empId(self, emp_id):
        pass
    @abstractmethod
    def get_employees_by_dept(self, dep_id):
        pass
    @abstractmethod
    def get_employees_by_gender(self, Gender):
        pass
    @abstractmethod
    def get_employees_order_by_salary(self, ascending=True):
        pass
