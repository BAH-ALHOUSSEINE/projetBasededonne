create table Region (
    codeReg varchar(2) constraint cle_region PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null
);

create table Departement (
    codeDep varchar(3) constraint cle_departement PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null,
    codeReg varchar(2) references Region(codeReg)
);

create table Commune (
    codeCom varchar(5) constraint cle_commune PRIMARY KEY,
    libelle varchar(200) constraint libelle_null not null,
    codeDep varchar(3) references Departement(codeDep)
);

create table ChefLieuRegion (
    codeReg varchar(2) references Region(codeReg),
    codeCom varchar(5) references Commune(codeCom),
    PRIMARY KEY(codeCom)
);

create table ChefLieuDepartement (
    codeDep varchar(3) references Departement(codeDep),
    codeCom varchar(5) references Commune(codeCom),
    PRIMARY KEY(codeCom)
);

create table StatCommuneAnnee (
    id varchar(200),
    annee int,
    codeCom varchar(5) references Commune(codeCom),
    valeur int,
    PRIMARY KEY(codeCom, id, annee)
);

create table StatCommuneIntervalle (
    id varchar(200),
    anneeDebut int,
    anneeFin int,
    codeCom varchar(5) references Commune(codeCom),
    valeur int,
    PRIMARY KEY(codeCom, id, anneeDebut, anneeFin)
);

