import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector as mysql

class dbmanager:
    def __init__(self) -> None:
        self.connector = mysql.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database =  os.getenv('DB_NAME')
        )

        self.cursor = self.connector.cursor()
        
    def __del__(self) -> None:
        self.cursor.close()
        self.connector.close()

    def query(self, qstring:str, qdata:tuple=()):
        self.cursor.execute(qstring, qdata)
        return self.cursor.fetchall()
    
    def insert(self, qstring:str, qdata:tuple=()):
        self.cursor.execute(qstring, qdata)
        self.connector.commit()
        return self.cursor.lastrowid

    def validate_exists(self, object, field):
        self.cursor.execute('SELECT * FROM {} WHERE {} = %s'.format(object, field), (field,))
        return self.cursor.fetchone() is not None
    
    def create_entry_hash(self, field, object):
        self.cursor.execute('SELECT * FROM {} WHERE {} = %s'.format(object, field), (field,))
        return self.cursor.fetchone()
    
    def update(self, qstring:str, qdata:tuple=()):
        self.cursor.execute(qstring, qdata)
        self.connector.commit()
        return self.cursor.rowcount
    
    