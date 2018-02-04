import app
import sqlite3
import os


if __name__ == '__main__':
    os.makedirs(os.path.dirname(app.database_path), exist_ok=True)
    conn = sqlite3.connect(app.database_path)
    conn.close()
