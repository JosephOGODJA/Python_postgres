CREATE TABLE boursier (
  Id_boursier SERIAL,
  Nom varchar(1024) DEFAULT NULL,
  PrenomBoursier varchar(1024) DEFAULT NULL,
  ID_statu_matimonial SERIAL,
  Coordonnees SERIAL,
  Formation SERIAL,
  Bourse SERIAL,
  ExperienceProfessionnelle SERIAL,
  Metier SERIAL,
  Sante SERIAL,
  PRIMARY KEY (Id_boursier),
  FOREIGN KEY (ID_statu_matimonial) REFERENCES statut_matrimonial(ID_statu_matimonial),
  FOREIGN KEY (Coordonnees) REFERENCES coordonnées(ID_coordonees),
  FOREIGN KEY (Formation) REFERENCES formation(ID_formation),
  FOREIGN KEY (Bourse) REFERENCES bourse(ID_bourse),
  FOREIGN KEY (ExperienceProfessionnelle) REFERENCES expérience_professionnelle(ID_experience_pro),
  FOREIGN KEY (Metier) REFERENCES metier(ID_metier),
  FOREIGN KEY (Sante) REFERENCES santé(ID_sante),
  UNIQUE(Id_boursier)
);
