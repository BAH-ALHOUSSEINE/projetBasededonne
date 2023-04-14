insert into Region(code, libelle) values (1, 'Guadeloupe');
insert into Departement(code, libelle,region) values (1, 'Guadeloupe',1);
insert into Commune(code, departement,libelle) values (1001,1, 'Guadeloupe');
insert into StatCommuneAnnee(id, annee, codeCommune,valeur) values ('population', 2019,1001,779 );