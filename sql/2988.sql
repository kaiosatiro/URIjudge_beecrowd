
select 	name,
		count(teams.id) as matches,
        
        count(case when team_1 = teams.id and team_1_goals > team_2_goals then 1 end) + 
        count(case when team_2 = teams.id and team_2_goals > team_1_goals then 1 end) as victories,
        
        count(case when team_1 = teams.id and team_1_goals < team_2_goals then 1 end) + 
        count(case when team_2 = teams.id and team_2_goals < team_1_goals then 1 end) as defeats,
        
        count(case when team_1_goals = team_2_goals then 1 end) as draws,
        
        ((count(case when team_1 = teams.id and team_1_goals > team_2_goals then 1 end) + 
        count(case when team_2 = teams.id and team_2_goals > team_1_goals then 1 end)) * 3)
        + 
        count(case when team_1_goals = team_2_goals then 1 end) as score
        
from matches
join teams on matches.team_1 = teams.id or matches.team_2 = teams.id
where teams.name in (select name from teams)
group by teams.name
order by score desc