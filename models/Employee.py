# Employee Model class / DB Entity Class

class Employees:
    def __init__(self, emp_id, emp_name, password, gender, dob, phone, email, salary, address, dep_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.password = password
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.email = email
        self.salary = salary
        self.address = address
        self.dep_id = dep_id