import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r'C:\Users\nikit\PycharmProjects\BGU_FAQ_BOT\database\mydatabase.db')
        self.cursor = self.connection.cursor()
        self.connection.execute(
            '''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                   name TEXT NOT NULL,
                                                   login TEXT,
                                                   password TEXT);'''
        )

    def save_data(self, log, password, user_id):
        with self.connection:
            self.cursor.execute("UPDATE users SET login=?, password=? WHERE user_id=?", (log, password, user_id))
            self.connection.commit()

    def forget_data(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE users SET login=?,password=? WHERE user_id=?", (None, None, user_id))
            self.connection.commit()

    def data_extsts(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()
            return result

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT 1 FROM users WHERE user_id=?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, nick):
        with self.connection:
            self.cursor.execute("REPLACE INTO users ('user_id','name') VALUES (?,?)", (user_id, nick))
            self.connection.commit()

    def all_users(self):
        self.cursor.execute('SELECT user_id FROM users')
        data = self.cursor.fetchall()
        text = []
        for row in data:
            text.append(f"{row[0]}")
        return text
