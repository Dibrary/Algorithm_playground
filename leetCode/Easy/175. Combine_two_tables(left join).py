

#이 문제는 SQL문제로 left join 쓰는 것.
'''

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address as a
ON p.personId=a.personId
ORDER BY p.firstName asc;

'''