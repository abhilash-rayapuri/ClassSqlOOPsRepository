from abc import ABC, abstractmethod

# Abstract Base Class for Department Repository
class EmpRepository(ABC):
    @abstractmethod
    def insert_employee(self,db_name, Employees):
        pass
    @abstractmethod
    def update_employee(self,db_name, Employees):
        pass
    @abstractmethod
    def delete_employee(self,db_name, emp_id):
        pass
    @abstractmethod
    def fetch_all_employees(self,db_name, Employees):
        pass
    @abstractmethod
    def fetch_employee_by_id(self,db_name, emp_id):
        pass
    @abstractmethod
    def fetch_employees_by_dept(self,db_name, dep_id):
        pass
    @abstractmethod
    def fetch_employees_by_gender(self,db_name, Gender):
        pass
    @abstractmethod
    def fetch_employees_order_by_salary(self,db_name, ascending=True):
        pass
