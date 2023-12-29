import sqlite3

DB_NAME = 'mouse_data.db'


async def save_to_database(x, y, image_path):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS mouse_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                x INTEGER,
                y INTEGER,
                image_path TEXT
            )
        ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO mouse_data (x, y, image_path)
        VALUES (?, ?, ?)
    ''', (x, y, image_path))

    conn.commit()
    conn.close()
