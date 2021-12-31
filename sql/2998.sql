--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2998

CREATE TABLE clients (
    id integer PRIMARY KEY,
    name varchar(50),
    investment numeric
);

CREATE TABLE operations (
    id integer PRIMARY KEY,
    client_id integer,
    month integer,
    profit numeric,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);
insert into clients (id,name,investment) values
(1,'Daniel',500),
(2,'Oliveira',2000),
(3,'Lucas',1000);


INSERT INTO operations (id, client_id, month, profit) VALUES
(1,1,1,230),
(2,2,1,1000),
(3,2,2,1000),
(4,3,1,100),
(5,3,2,300),
(6,3,3,900),
(7,3,4,400);

/*  Execute this query to drop the tables */
-- DROP TABLE operations;
-- DROP TABLE clients;


select	id
		, client_id
		, month
		, profit
		, sum(profit) over(partition by client_id) as soma_total
		, last_value(profit) over(partition by client_id, month) as last_value
from operations
group by id, client_id, month, profit
order by client_id, month


select  cl.name
		, cl.investment
		, cl.id 
from clients cl	
join operations op on cl.id = op.client_id 
group by cl.name, cl.investment, op.client_id, cl.id
having sum(op.profit) >= cl.investment


select  clients.name
		, clients.investment
        , case 	when (operations.soma - operations.last_value - clients.investment) < 0 then max(operations.month) 
				else (max(operations.month) - 1) 
				end as month_of_payback            
        , case 	when (operations.soma - operations.last_value - clients.investment) < 0 
				then 0 else (operations.soma - operations.last_value - clients.investment) 
				end as return
        
from 	(select	 client_id, month, last_value(profit) over(partition by client_id) as last_value, sum(profit) over(partition by client_id) as soma	from operations)
			operations,
			
		(select  cl.name, cl.investment, cl.id from clients cl	join operations op on cl.id = op.client_id group by cl.name, cl.investment, cl.id
				  having sum(op.profit) >= cl.investment)
			clients 
where clients.id = operations.client_id
group by clients.name, clients.investment, operations.soma, operations.last_value
order by return desc