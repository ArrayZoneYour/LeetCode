SELECT d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary FROM Employee e1
  JOIN Department d ON e1.DepartmentId = d.Id
  JOIN Employee e2 ON e1.DepartmentId = e2.DepartmentId
WHERE e2.Salary >= e1.Salary
GROUP BY d.Name, e1.Name HAVING count(DISTINCT e2.Salary) <= 3
ORDER BY d.Name, e1.Salary DESC