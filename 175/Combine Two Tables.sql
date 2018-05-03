# /usr/bin/python
# coding: utf-8


# Write your MySQL query statement below
SELECT FirstName, LastName, City, State FROM Person LEFT OUTER JOIN Address on Person.PersonId = Address.PersonId