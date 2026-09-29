INSERT INTO heroes (nombre, clase, nivel_experiencia) VALUES
    ('Aragorn', 'Guerrero', 15),
    ('Gandalf', 'Mago', 20),
    ('Legolas', 'Arquero', 14),
    ('Elara', 'Clériga', 9);

INSERT INTO misiones (nombre, nivel_dificultad, localizacion, recompensa_oro) VALUES
    ('Rescate en la Montaña Roja', 8, 'Montaña Roja', 1500),
    ('Limpieza de la Cripta', 5, 'Cripta Olvidada', 600),
    ('Patrulla del Bosque', 2, 'Bosque Umbrío', 150);

INSERT INTO monstruos (nombre, tipo, nivel_amenaza) VALUES
    ('Ignis', 'Dragón', 10),
    ('Grok', 'Goblin', 2),
    ('Rey Lich', 'No-muerto', 8),
    ('Esqueleto Guardián', 'No-muerto', 4);

INSERT INTO heroe_mision (heroe_id, mision_id) VALUES
    (1, 1), (2, 1), (3, 1),
    (2, 2), (4, 2),
    (1, 3), (3, 3);

INSERT INTO mision_monstruo (mision_id, monstruo_id) VALUES
    (1, 1), (1, 2),
    (2, 3), (2, 4),
    (3, 2);
