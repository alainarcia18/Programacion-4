PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS mision_monstruo;
DROP TABLE IF EXISTS heroe_mision;
DROP TABLE IF EXISTS monstruos;
DROP TABLE IF EXISTS misiones;
DROP TABLE IF EXISTS heroes;

CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clase TEXT NOT NULL,
    nivel_experiencia INTEGER NOT NULL CHECK (nivel_experiencia >= 1)
);

CREATE TABLE misiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel_dificultad INTEGER NOT NULL CHECK (nivel_dificultad BETWEEN 1 AND 10),
    localizacion TEXT NOT NULL,
    recompensa_oro INTEGER NOT NULL CHECK (recompensa_oro >= 0)
);

CREATE TABLE monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    nivel_amenaza INTEGER NOT NULL CHECK (nivel_amenaza BETWEEN 1 AND 10)
);

CREATE TABLE heroe_mision (
    heroe_id INTEGER NOT NULL,
    mision_id INTEGER NOT NULL,
    PRIMARY KEY (heroe_id, mision_id),
    FOREIGN KEY (heroe_id) REFERENCES heroes(id) ON DELETE CASCADE,
    FOREIGN KEY (mision_id) REFERENCES misiones(id) ON DELETE CASCADE
);

CREATE TABLE mision_monstruo (
    mision_id INTEGER NOT NULL,
    monstruo_id INTEGER NOT NULL,
    PRIMARY KEY (mision_id, monstruo_id),
    FOREIGN KEY (mision_id) REFERENCES misiones(id) ON DELETE CASCADE,
    FOREIGN KEY (monstruo_id) REFERENCES monstruos(id) ON DELETE CASCADE
);
