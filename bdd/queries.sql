--Vue population des départements

create view population_année_departement as
Select SUM(stat.valeur) as pop, stat.annee, d.codeDep
from StatCommuneAnnee stat, Departement d, Commune c
where stat.id = 'population' and c.codeCom = stat.codeCom and c.codeDep = d.codeDep
GROUP BY (d.codeDep, stat.annee);

drop view population_année_departement;

select * from population_année_departement vue
where vue.annee = '2019' and vue.codeDep = '12';


--Vue population des régions

create view population_année_region as
Select SUM(popDep.pop), d.codeReg, popDep.annee
from population_année_departement as popDep, Departement d
where popDep.codeDep = d.codeDep
GROUP BY (d.codeReg, popDep.annee);

drop view population_année_region;

select * from population_année_region vue
where vue.annee = '2019' and vue.codeReg = '76';


--Ajout de population dans les tables régions et départements

ALTER TABLE Departement
ADD population INT;

ALTER TABLE Region
ADD population INT;

--Procedure stocké

CREATE PROCEDURE calculerSalaireMoyen(IN dep VARCHAR(3), OUT salaireMoyen DECIMAL(10,2))
BEGIN
    SELECT AVG(salaire_annuel) INTO salaireMoyen FROM employes WHERE departement = dep;
END;