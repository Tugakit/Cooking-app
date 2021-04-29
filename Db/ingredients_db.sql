CREATE TABLE ingredients (
id_ingredients			INT					NOT NULL PRIMARY KEY AUTO_INCREMENT,
nom_ingredients			VARCHAR(25)			NOT NULL,
quantites				FLOAT				NOT NULL,
id_mesure				INT					NOT NULL,
id_recette				INT					NOT NULL,
FOREIGN KEY (id_recette) REFERENCES Recettes(id_Recette),
FOREIGN KEY (id_mesure) REFERENCES mesures(id_mesures)
);