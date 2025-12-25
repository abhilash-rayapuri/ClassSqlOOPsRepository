from abc import ABC, abstractmethod

# Abstract Base Class for Department Repository
class DeptRepository(ABC):
    @abstractmethod
    def insert_department(self, departments):
        pass

    @abstractmethod
    def update_department(self, departments):
        pass

    @abstractmethod
    def delete_department(self, dep_id):
        pass

    @abstractmethod
    def get_all_departments(self):
        pass

    @abstractmethod
    def get_department_by_deptNo(self, dep_id):
        pass

    @abstractmethod
    def get_departments_by_dname(self, dep_name):
        pass