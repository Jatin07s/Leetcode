# Write your MySQL query statement below
select 
    d.name as Department ,
    e.name as Employee ,
    e.salary as Salary
    from (
        select 
        id,
        name,
        salary ,
        departmentId ,
        dense_rank() over (
            partition by departmentId
            order by salary desc
        ) as rnk
        from Employee
    ) as e
    inner join Department as d
    on e.departmentId = d.id
    where rnk = 1;
