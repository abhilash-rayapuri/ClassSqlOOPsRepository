class DeptService:
    def __init__(self, dept_repository):
        self.dept_repository = dept_repository

    def Insert_department(self, departments):
        return self.dept_repository.insert_department(departments)
    
    def Update_department(self, departments):
        return self.dept_repository.update_department(departments)
    
    def Delete_department(self, dep_id):
        return self.dept_repository.delete_department(dep_id)
    
    def Get_all_departments(self):
        return self.dept_repository.get_all_departments()
    
    def Get_department_by_deptNo(self, dep_id):
        return self.dept_repository.get_department_by_dept_no(dep_id)
    
    def Get_departments_by_dname(self, dep_name):
        return self.dept_repository.get_departments_by_dname(dep_name)