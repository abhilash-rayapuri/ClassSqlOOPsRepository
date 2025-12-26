from .Dept_Repository import DeptRepository

class DeptRepositoryImpl(DeptRepository):   
    def __init__(self, connection):
        self.connection = connection
        
    def insert_department(self, departments):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO Department (Dep_id, Dep_name, Location) VALUES (%s, %s, %s)"
        try:
            cursor.execute(insert_query, (departments.dep_id, departments.dep_name, departments.location))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()

    def update_department(self, departments):
        cursor = self.connection.cursor()
        update_fields = []
        params = []
        if departments.dname:
            update_fields.append("dep_name = %s")
            params.append(departments.dep_name)
        if departments.location:
            update_fields.append("Location = %s")
            params.append(departments.location)
        params.append(departments.dep_id)  # For the WHERE clause
        update_query = f"UPDATE Departments SET {', '.join(update_fields)} WHERE Dep_id = %s"
        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            cursor.close()

    def delete_department(self, dep_id):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Departments WHERE DeptNo = %s"
        try:
            cursor.execute(delete_query, (dep_id,))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()

    def get_all_departments(self):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Departments"
        try:
            cursor.execute(select_query)
            deptList = cursor.fetchall()
            return deptList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()


    def get_department_by_deptNo(self, dep_id):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Departments WHERE Dep_id = %s"
        try:
            cursor.execute(select_query, (dep_id,))
            dept = cursor.fetchone()
            return dept
        except Exception as e:
            print(f"Error fetching record: {e}")
            return None
        finally:
            cursor.close()

    def get_departments_by_dname(self, dep_name):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Departments WHERE Dep_name = %s"
        try:
            cursor.execute(select_query, (dep_name,))
            deptList = cursor.fetchall()
            return deptList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()