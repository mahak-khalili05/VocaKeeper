import sqlite3


def get_connection():
    conn = sqlite3.connect("vocabulary.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        korean TEXT NOT NULL,
        persian TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


create_table()


def add_word(korean, persian):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO words(korean, persian) VALUES (?, ?)",
        (korean, persian)
    )

    conn.commit()
    conn.close()


def show_words():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM words")

    words = cursor.fetchall()

    conn.close()

    return words


def search_word(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM words WHERE korean LIKE ? OR persian LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )

    words = cursor.fetchall()

    conn.close()

    return words


def delete_word(word_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM words WHERE id=?",
        (word_id,)
    )

    conn.commit()
    conn.close()
