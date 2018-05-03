# /usr/bin/python
# coding: utf-8


# Write your MySQL query statement below
SELECT max(Salary) as SecondHighestSalary FROM Employee WHERE Salary < (SELECT max(Salary) FROM Employee)
