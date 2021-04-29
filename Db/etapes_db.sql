CREATE TABLE etapes (
id_etape				INT					NOT NULL PRIMARY KEY AUTO_INCREMENT,
id_recette				INT					NOT NULL,
description				LONGTEXT			NOT NULL,
FOREIGN KEY (id_recette) REFERENCES Recettes(id_Recette)
);