# Write your MySQL query statement below

update SALARY 
set sex = Case 
    when sex = 'f' then 'm'
    when sex = 'm' then 'f'
    end;
