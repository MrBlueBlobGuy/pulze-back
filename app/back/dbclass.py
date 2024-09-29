import sqlite3 as sql
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.addHandler(logging.StreamHandler())

class DB:
    def __init__(self):
        self.conn = sql.connect(os.getenv("DB_PATH"))
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, phonenumber TEXT, password TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS messages (senderid TEXT, receiverid TEXT, message TEXT, status TEXT, timestamp INTEGER, messageid TEXT)")
        self.conn.commit()

    def add_user(self, name, phonenumber, password):
        try:
            self.cursor.execute("INSERT INTO users (name, phonenumber, password) VALUES (?, ?, ?)", (name, phonenumber, password))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(e)
            return False

    def get_user(self, name, password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            logger.error(e)
            return None

    def add_message(self, senderid, receiverid, message, status, timestamp, messageid):
        try:
            self.cursor.execute("INSERT INTO messages (senderid, receiverid, message, status, timestamp, messageid) VALUES (?, ?, ?, ?, ?, ?)", (senderid, receiverid, message, status, timestamp, messageid))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(e)
            return False

    def get_messages(self, senderid, receiverid):
        try:
            self.cursor.execute("SELECT * FROM messages WHERE senderid=? AND receiverid=?", (senderid, receiverid))
            messages = self.cursor.fetchall()
            return messages
        except Exception as e:
            logger.error(e)
            return None

    def get_all_messages(self):
        try:
            self.cursor.execute("SELECT * FROM messages")
            messages = self.cursor.fetchall()
            return messages
        except Exception as e:
            logger.error(e)
            return None