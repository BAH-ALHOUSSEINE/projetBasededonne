--Vue population des départements
drop view population_année_region;
drop view population_année_departement;
create view population_année_departement as
Select SUM(stat.valeur) as pop, stat.annee, d.codeDep
from StatCommuneAnnee stat, Departement d, Commune c
where stat.id = 'population' and c.codeCom = stat.codeCom and c.codeDep = d.codeDep
GROUP BY (d.codeDep, stat.annee);






--Vue population des régions

create view population_année_region as
Select SUM(popDep.pop) as pop, d.codeReg, popDep.annee
from population_année_departement as popDep, Departement d
where popDep.codeDep = d.codeDep
GROUP BY (d.codeReg, popDep.annee);



select * from population_année_departement vue
where vue.annee = '2019' and vue.codeDep = '12';


select * from population_année_region vue
where vue.annee = '2019' and vue.codeReg = '76';


--Ajout de population dans les tables régions et départements

ALTER TABLE Departement
ADD population INT;

ALTER TABLE Region
ADD population INT;

--Procedure stocké

--Departement
CREATE PROCEDURE calculerPopulationDepartement
()
LANGUAGE SQL
AS $$
update Departement set population = (SELECT pop FROM population_année_departement vue WHERE vue.codeDep = Departement.codeDep and vue.annee = '2019');
$$;

call calculerPopulationDepartement();
select population from Departement;

--Region
create Procedure calculerPopulationRegion
()
LANGUAGE SQL
AS $$
update Region set population = (SELECT pop FROM population_année_region vue WHERE vue.codeReg = Region.codeReg and vue.annee = '2019');
$$;

call calculerPopulationRegion();
select population from Region;
*/