# SELECT DISTINCT a.Num as ConsecutiveNums FROM Logs a
# JOIN Logs b on a.Id = (b.Id + 1)
# JOIN Logs c on a.Id = (c.Id + 2)
# WHERE (a.Num = b.Num) AND (b.Num = c.Num)

SELECT DISTINCT Num as ConsecutiveNums FROM Logs, (SELECT @pre:=null, @cnt:=0) t2
WHERE (
  CASE
  WHEN @cnt = 2 AND Num = @pre then (@cnt:=0) || 1
  WHEN Num = @pre then (@cnt:=@cnt+1) && 0
  ELSE (@cnt := (@cnt || 1)) && (@pre:=Num) && 0
  END
) > 0