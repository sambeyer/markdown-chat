import sqlite3
import sqlite_vss
import os
import hashlib


def setup_database(db_name):
    db = sqlite3.connect(db_name)
    db.enable_load_extension(True)
    sqlite_vss.load(db)
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS embeddings (
            id TEXT PRIMARY KEY,
            file_name TEXT,
            content TEXT,
            embedding TEXT
        )
    """
    )
    db.commit()
    db.close()


def insert_embedding(db_name, file_path, content, embedding):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Hash file name
    file_name = os.path.basename(file_path)
    file_id = hashlib.sha256(content.encode()).hexdigest()

    # Convert embedding to a string
    embedding_str = ",".join(map(str, embedding))

    cursor.execute(
        """
        INSERT OR IGNORE INTO embeddings (id, file_name, content, embedding)
        VALUES (?, ?, ?, ?)
    """,
        (file_id, file_name, content, embedding_str),
    )
    conn.commit()
    conn.close()
