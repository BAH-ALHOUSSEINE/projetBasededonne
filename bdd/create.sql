create table Region (
    code varchar(2) constraint cle_region PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null
);

create table Departement (
    code varchar(3) constraint cle_departement PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null,
    region varchar(2) references Region(code)
);

create table Commune (
    code varchar(5) constraint cle_commune PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null,
    departement varchar(3) references Departement(code)
);

create table ChefLieuRegion (
    code varchar(2) references Region(code),
    commune varchar(5) references Commune(code),
    PRIMARY KEY(code)
);

create table ChefLieuDepartement (
    code varchar(3) references Departement(code),
    commune varchar(5) references Commune(code),
    PRIMARY KEY(code)
);

create table StatCommuneAnnee (
    id varchar(200),
    annee int,
    codeCommune varchar(5) references Commune(code),
    valeur int,
    PRIMARY KEY(codeCommune, id, annee)
);

create table StatCommuneIntervalle (
    id varchar(200),
    anneeDebut int,
    anneeFin int,
    codeCommune varchar(5) references Commune(code),
    valeur int,
    PRIMARY KEY(codeCommune, id, anneeDebut, anneeFin)
);

