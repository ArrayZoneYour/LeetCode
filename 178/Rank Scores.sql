# /usr/bin/python
# coding: utf-8


# SELECT Score, dense_rank() OVER (ORDER BY Score desc) Rank FROM Scores ORDER BY Score DESC

SELECT Scores.score AS Score, rank.rankid AS Rank FROM Scores LEFT JOIN
  (SELECT @rowid:= @rowid + 1 AS rankid, temp1.score FROM
    (SELECT DISTINCT Score FROM Scores ORDER BY Score DESC) AS temp1,
    (SELECT @rowid:= 0) AS temp2) AS rank
  ON Scores.score = rank.Score ORDER BY Rank