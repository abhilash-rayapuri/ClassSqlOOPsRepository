from Emp_Repository import EmpRepository

class EmpRepositoryImpl(EmpRepository):
    def __init__(self, connection):
        self.connection = connection

    def insert_employee(self, db_name, Employees):
        cursor = self.connection.cursor()
        insert_query = """INSERT INTO Employees
                              (Emp_Id, Emp_name, Password, Gender, Dob, Phone, Email, Salary, Address, Dept_id) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            cursor.execute(insert_query,
                           (Employees.emp_id, Employees.emp_name, Employees.Password, Employees.Gender, Employees.Dob, Employees.Phone, Employees.Email, Employees.Salary, Employees.Address, Employees.dep_id))
            self.connection.commit()  # Commit the transaction to save changes
            print("Employee record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()
            self.connection.close()

    def update_employee(self, db_name, Employees):
        cursor = self.connection.cursor()
        update_fields = []
        params = []
        if Employees.emp_name:
            update_fields.append("emp_name = %s")
            params.append(Employees.emp_name)
        if Employees.Password:
            update_fields.append("Password = %s")
            params.append(Employees.Password)
        if Employees.Gender:
            update_fields.append("Gender = %s")
            params.append(Employees.Gender)
        if Employees.Dob:
            update_fields.append("Dob = %s")
            params.append(Employees.Dob)
        if Employees.Phone:
            update_fields.append("Phone = %s")
            params.append(Employees.Phone)
        if Employees.Email:
            update_fields.append("Email = %s")
            params.append(Employees.Email)
        if Employees.Salary is not None:
            update_fields.append("Salary = %s")
            params.append(Employees.Salary)
        if Employees.Address:
            update_fields.append("Address = %s")
            params.append(Employees.Address)
        if Employees.dep_id is not None:
            update_fields.append("dep_id = %s")
            params.append(Employees.dep_id)
        params.append(Employees.emp_id)
        update_query = f"UPDATE Employees SET {', '.join(update_fields)} WHERE emp_id = %s"
        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit()  # Commit the transaction to save changes
            print("Employee record updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            cursor.close()
            self.connection.close()

    def delete_department(self, emp_id):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Employees WHERE emp_id = %s"
        try:
            cursor.execute(delete_query, (emp_id,))
            self.connection.commit()  # Commit the transaction to save changes
            print("Employee record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()
            self.connection.close()

    def fetch_all_employees(self, db_name, employees):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employees"
        try:
            cursor.execute(select_query)
            empList = cursor.fetchall()
            return empList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()

    def fetch_employee_by_id(self, db_name, emp_id):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employees WHERE emp_id = %s"
        try:
            cursor.execute(select_query, (emp_id,))
            emp = cursor.fetchone()
            return emp
        except Exception as e:
            print(f"Error fetching record: {e}")
            return None
        finally:
            cursor.close()
            self.connection.close()

    def fetch_employees_by_dept(self, db_name, dep_id):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employees WHERE Dep_id = %s"
        try:
            cursor.execute(select_query, (dep_id,))
            empDeptList = cursor.fetchall()
            return empDeptList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()

    def fetch_employees_by_gender(self, db_name, Gender):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employees WHERE Gender = %s"
        try:
            cursor.execute(select_query, (Gender,))
            empGenderList = cursor.fetchall()
            return empGenderList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()

    def fetch_employees_order_by_salary(self, db_name, ascending=True):
        cursor = self.connection.cursor()
        order = "DESC" if not ascending else "ASC"
        select_query = f"SELECT * FROM Employees ORDER BY Salary {order}"
        try:
            cursor.execute(select_query)
            empSalaryList = cursor.fetchall()
            return empSalaryList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()