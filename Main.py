from db.MySqlConnection import MySqlConnection
from repositories.Dept_Repository_Impl import DeptRepositoryImpl
from repositories.Emp_Repository_Impl import EmpRepositoryImpl
from models.Department import Departments
from models.Employee import Employees
from services.Dept_Service import DeptService
from services.Emp_Services import EmpService

def Department_CRUD_Operations():
    connection = MySqlConnection().get_connection()
    deptRepository = DeptRepositoryImpl(connection)
    deptService = DeptService(deptRepository)

    print("\nDepartment CRUD Operations : ")
    print("1. Insert Department Record")
    print("2. Update Department Record")
    print("3. Delete Department Record")
    print("4. Fetch All Department Records")
    print("5. Fetch Department Record by DeptNo")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:        
        dep_id = int(input("Enter Dep_id: "))
        dep_name = input("Enter Dep_name: ")
        location = input("Enter Location: ")
        dept = Departments(dep_id, dep_name, location)
        #Validate DeptNo and Dname before insertion
        deptValid = deptService.Get_department_by_deptNo(dept.dep_id)      
        if deptValid:
            print("Already Department with this Dep_id exists. Cannot insert duplicate Dep_id.")
        else:
            deptValid = deptService.Get_departments_by_dname(dept.dep_name)
            if deptValid:
                print("Already Department with this Dep_name exists. Cannot insert duplicate Dep_name.")
            else:
                deptService.Insert_department(dept)
    elif choice == 2:        
        dep_id = int(input("Enter Dep_id to update: "))
        dep_name = input("Enter new Dep_name (leave blank to skip): ")
        location = input("Enter new Location (leave blank to skip): ")
        dept = Departments(dep_id, dep_name, location)
        deptService.Update_department(dept)
    elif choice == 3:
        dep_id = int(input("Enter Dep_id to delete: "))
        deptService.Delete_department(dep_id)
    elif choice == 4:
        deptList = deptService.Get_all_departments()
        for dept in deptList:
            print(dept)
    elif choice == 5:
        dep_id = int(input("Enter Dep_id to fetch: "))
        dept = deptService.Get_department_by_deptNo(dep_id)
        if dept:
            print(dept)
        else:
            print("Department not found.")

    connection.close()

def Employee_CRUD_Operations():
    connection = MySqlConnection().get_connection()
    empRepository = EmpRepositoryImpl(connection)
    empService = EmpService(empRepository)

    print("\nEmployee CRUD Operations : ")
    print("1. Insert Employee Record")
    print("2. Update Employee Record")
    print("3. Delete Employee Record")
    print("4. Fetch All Employee Records")
    print("5. Fetch Employee Record by EmpId")
    print("6. Fetch Employees by Dep_id")
    print("7. Fetch Employees by Gender")
    print
    choice = int(input("Enter your choice (1-8): "))
    if choice == 1:        
        emp_id = int(input("Enter Emp_Id: "))
        emp_name = input("Enter Emp_name: ")
        Password = input("Enter Password: ")
        Gender = input("Enter Gender: ")
        Dob = input("Enter Dob (YYYY-MM-DD): ")
        Phone = input("Enter Phone: ")
        Email = input("Enter Email: ")
        Salary = float(input("Enter Salary: "))
        Address = input("Enter Address: ")
        Dep_id = int(input("Enter Dept_id: "))
        emp=Employees(emp_id, emp_name, Password, Gender, Dob, Phone, Email, Salary, Address, Dep_id)
        # Validate EmpId before insertion
        empValid = empService.get_employee_by_empId(emp_id)
        if empValid:
            print("Already Employee with this EmpId exists. Cannot insert duplicate EmpId.")
        else: 
            empService.insert_employee(emp)
    elif choice == 2:
        emp_id = int(input("Enter emp_id to update: "))
        emp_name = input("Enter new emp_id (leave blank to skip): ")
        Password = input("Enter new Password (leave blank to skip): ")
        Gender = input("Enter new Gender (leave blank to skip): ")
        Dob = input("Enter new Dob (YYYY-MM-DD) (leave blank to skip): ")
        Phone = input("Enter new Phone (leave blank to skip): ")
        Email = input("Enter new Email (leave blank to skip): ")
        Salary_input = input("Enter new Salary (leave blank to skip): ")
        Salary = float(Salary_input) if Salary_input else None
        Address = input("Enter new Address (leave blank to skip): ")
        dep_id_input = input("Enter new dep_id (leave blank to skip): ")
        dep_id = int(dep_id_input) if dep_id_input else None
        emp=Employees(emp_id, emp_name if emp_name else None, Password if Password else None, Gender if Gender else None, Dob if Dob else None, Phone if Phone else None, Email if Email else None, Salary if Salary else None, Address if Address else None, dep_id if dep_id else None)
        empService.update_employee(emp) 
    elif choice == 3:
        emp_id = int(input("Enter emp_id to delete: "))
        empService.delete_employee(emp_id)
    elif choice == 4:
        empList = empService.get_all_employees(emp_id)
        for emp in empList:
            print(emp)
    elif choice == 5:
        emp_id = int(input("Enter emp_id to fetch: "))
        emp = empService.get_employee_by_empId(emp_id)
        if emp:
            print(emp)
        else:
            print("Employee not found.")
    elif choice == 6:
        dep_id = int(input("Enter dep_id to fetch employees: "))
        empList = empService.get_employees_by_deptNo(dep_id)
        for emp in empList:
            print(emp)
    elif choice == 7:
        gender = input("Enter gender to fetch employees: ")
        empList = empService.get_employees_by_gender(gender)
        for emp in empList:
            print(emp)
    elif choice == 8:
        order_choice = input("Enter 'A' for ascending or 'D' for descending order by salary: ")
        ascending = True if order_choice.upper() == 'A' else False
        empList = empService.get_employees_order_by_salary(ascending)
        for emp in empList:
            print(emp)
    
    else:
        print("Invalid choice. Please select a valid operation.")
    
    connection.close()

        


print("\n\nStart CRUD Operations Using OOPs : ")
ch = input("Which Table CRUD Operations do you want perform (Department - 'D' / Employee - 'E'): ")
if (ch.upper() == "D"):
    # Perform Department DRUD Operations
    Department_CRUD_Operations()
elif (ch.upper() == "E"):
    #Perform Employee CRUD Operations
    Employee_CRUD_Operations()
else:
    print("Invalid operations...!\nPlease enter proper operation...!")

# match(ch.upper()):
#     case 'D':
#         Perform Department DRUD Operations
#         Department_CRUD_Operations()
#     case 'E':
#         Perform Employee CRUD Operations
#         Employee_CRUD_Operations()
#     case _:
#         print("Invalid operations...!\nPlease enter proper operation...!")

print("End of CRUD Operations...!")
