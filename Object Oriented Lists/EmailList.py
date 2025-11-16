import random


class Employee:

    # self.__FirstName string
    # self.__LastName string
    # self.__FullName string
    # self.__Email string
    # self.__EmployeeID string
    def __init__(self, FirstName, LastName, EmployeeID):
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__FullName = FirstName + " " + LastName
        self.__Email = FirstName.lower() + "." + LastName.lower() + "@company.com"
        self.__EmployeeID = EmployeeID

    def GetEmployeeEmail(self, EmployeeID):
        for i in range(9):
            if list_of_employees[i].__EmployeeID == EmployeeID:
                return self.__Email
        return "Employee not found"


list_of_employees = []
list_of_employeeIDs = []


with open("EmailList.txt", "r") as file:
    for i in range(9):
        FirstName = file.readline().strip()
        LastName = file.readline().strip()

        EmployeeID = random.randint(1, 9)
        while EmployeeID in list_of_employeeIDs:
            EmployeeID = random.randint(1, 9)

        employee_object = Employee(FirstName, LastName, EmployeeID)
        list_of_employees.append(employee_object)