CREATE TABLE types_recettes (
id_type_recettes		INT					NOT NULL PRIMARY KEY AUTO_INCREMENT,
id_recette				INT					NOT NULL,
FOREIGN KEY (id_recette) REFERENCES Recettes(id_Recette)
);