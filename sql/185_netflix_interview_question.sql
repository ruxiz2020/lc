select D.NAME AS Department, E1.Name as Employee, E1.Salary as Salary
FROM Employee as E1, Department as D
WHERE
(
SELECT Count(Distinct E2.Salary)
FROM Employee as E2
WHERE E1.DepartmentId = E2.DepartmentId
AND E2.Salary > E1.Salary
) < 3
AND E1.DepartmentId = D.Id;
