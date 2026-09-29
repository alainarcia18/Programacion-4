import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "gremio.db"


def ejecutar_script(conn, archivo):
    conn.executescript((BASE / archivo).read_text(encoding="utf-8"))


def mostrar(titulo, filas):
    print(f"\n== {titulo} ==")
    for fila in filas:
        print(fila)


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")  # necesario en cada conexión

    ejecutar_script(conn, "schema.sql")
    ejecutar_script(conn, "datos.sql")
    conn.commit()

    cur = conn.cursor()

    cur.execute("""
        SELECT m.nombre, h.nombre, h.clase
        FROM misiones m
        JOIN heroe_mision hm ON hm.mision_id = m.id
        JOIN heroes h ON h.id = hm.heroe_id
        ORDER BY m.nombre
    """)
    mostrar("Héroes por misión", cur.fetchall())

    cur.execute("""
        SELECT m.nombre, mo.nombre, mo.tipo, mo.nivel_amenaza
        FROM misiones m
        JOIN mision_monstruo mm ON mm.mision_id = m.id
        JOIN monstruos mo ON mo.id = mm.monstruo_id
        ORDER BY m.nombre
    """)
    mostrar("Monstruos por misión", cur.fetchall())

    cur.execute("""
        SELECT h.nombre, COUNT(hm.mision_id) AS total_misiones,
               COALESCE(SUM(m.recompensa_oro), 0) AS oro_total
        FROM heroes h
        LEFT JOIN heroe_mision hm ON hm.heroe_id = h.id
        LEFT JOIN misiones m ON m.id = hm.mision_id
        GROUP BY h.id
        ORDER BY oro_total DESC
    """)
    mostrar("Misiones y oro por héroe", cur.fetchall())

    conn.close()


if __name__ == "__main__":
    main()
