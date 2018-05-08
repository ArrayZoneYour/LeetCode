# Simple Solution
DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id
# Solution 2
DELETE FROM Person WHERE Id NOT IN
                         (SELECT Id FROM (SELECT min(Id) AS Id FROM Person GROUP BY Email) p);