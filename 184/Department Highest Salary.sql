SELECT Department.Name AS Department, e1.Name AS Employee, Salary FROM Employee e1, Department
WHERE e1.DepartmentId = Department.Id AND Salary >= ALL (
  SELECT Salary FROM Employee e2 WHERE e2.DepartmentId = e1.DepartmentId
)