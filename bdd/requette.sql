
--ecrit un fonction qui prend en parametre  le code de la region 

select departement.libelle from  departement WHERE region=?;

--ecrit un fonction qui prend en parametre  le nombre habitans et code departelmeent 

SELECT codeCommune, habitants
FROM StatCommuneAnnee
WHERE codeCommune IN (
    SELECT code
    FROM Commune
    WHERE codeDepartement = ?
) AND habitants > ?? ;

--ecrit une fonction qui prend le code du departement

SELECT code, libelle, habitants 
FROM Commune c
INNER JOIN StatCommuneAnnee s ON c.code = s.codeCommune
WHERE departement = ? -- Remplacez '01' par le code du département souhaité
ORDER BY habitants DESC
LIMIT 10; -- Remplacez '10' par le nombre de communes souhaité


--vue departement 
CREATE VIEW departements_population AS 
select annee ,sum(sa.habitants)  from departement  d JOIN commune c ON d.code=c.departement JOIN StatCommuneAnnee sa ON c.code=sa.codeCommune  GROUP BY d.code,sa.annee;

--vue region 

CREATE OR REPLACE VIEW PopulationRegions AS
SELECT r.code AS CodeRegion, r.libelle AS LibelleRegion, s.annee, SUM(s.habitants) AS Population
FROM Region r
INNER JOIN Departement d ON r.code = d.region
INNER JOIN Commune c ON d.code = c.departement
INNER JOIN StatCommuneAnnee s ON c.code = s.codeCommune
GROUP BY r.code, s.annee;




