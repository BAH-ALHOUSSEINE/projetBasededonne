create view population_année_departement as
Select SUM(stat.valeur) as pop, stat.annee, d.codeDep
from StatCommuneAnnee stat, Departement d, Commune c
where stat.id = 'population' and c.codeCom = stat.codeCom and c.codeDep = d.codeDep
GROUP BY (d.codeDep, stat.annee);

create view population_année_region as
Select SUM(popDep.pop), d.codeReg, popDep.annee
from population_année_departement as popDep, Departement d
where popDep.codeDep = d.codeDep
GROUP BY (d.codeReg, popDep.annee);


drop view population_année_departement;
drop view population_année_region;


select * from population_année_departement vue
where vue.annee = '2019' and vue.codeDep = '12';

select * from population_année_region vue
where vue.annee = '2019' and vue.codeReg = '76';