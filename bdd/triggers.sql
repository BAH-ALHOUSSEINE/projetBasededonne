--DROP TRIGGER IF EXISTS block_departement_modifications  ON departement;
--DROP TRIGGER IF EXISTS block_region_modifications ON region;


CREATE OR REPLACE FUNCTION bloque_modifications_departement()
RETURNS trigger AS
$$
BEGIN
    RAISE EXCEPTION 'Les modifications sur la table DEPARTEMENT sont interdites.';
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER block_departement_modifications
BEFORE INSERT OR UPDATE OR DELETE ON DEPARTEMENT
FOR EACH ROW
EXECUTE FUNCTION bloque_modifications_departement();


--pour la table region 

CREATE OR REPLACE FUNCTION bloque_modifications_region()
RETURNS trigger AS
$$
BEGIN
    RAISE EXCEPTION 'Les modifications sur la table Region sont interdites.';
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER block_region_modifications
BEFORE INSERT OR UPDATE OR DELETE ON Region
FOR EACH ROW
EXECUTE FUNCTION bloque_modifications_departement();



DROP TRIGGER IF EXISTS maj_population_region ON StatCommuneAnnee;

--AJOUTER Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour la population d'un département/région quand la population d'une ville est mise à jour.
--pour regi



CREATE OR REPLACE FUNCTION modifications_population_region()
RETURNS trigger AS
$$
BEGIN
    DROP TRIGGER IF EXISTS block_departement_modifications  ON departement;
    DROP TRIGGER IF EXISTS block_region_modifications ON region;

    call calculerPopulationDepartement();
    call calculerPopulationRegion() ;

    RETURN NULL;
END;
$$
LANGUAGE plpgsql;


CREATE TRIGGER maj_population_region
AFTER UPDATE ON StatCommuneAnnee
FOR EACH ROW
EXECUTE FUNCTION modifications_population_region();

UPDATE  StatCommuneAnnee
SET valeur = 1256458
WHERE codeCom = '75056' AND annee=2019;

