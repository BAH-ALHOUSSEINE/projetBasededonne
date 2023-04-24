create view population_année_departement as
Select d.code, SUM(stat.valeur) from StatCommuneAnnee stat, Commune c, Departement d
where annee = @date_annee and id = "population" and c.departement = @codeDep
group by Departement.code;