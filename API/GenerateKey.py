import hashlib
from MarsWeather import DBConnection
import os
from datetime import datetime

class GenerateKey():
    def __init__(self):
        self.__key = os.urandom(24).hex()
        self.__hash =  hashlib.sha256(self.__key.encode()).hexdigest()
        self.__date = datetime.now().strftime('%Y-%m-%d')

    def addUserKey(self, username:str, conn: DBConnection):
        conn.connect()
        conn.execute(f"""INSERT INTO api_keys (api_key_hash, date_of_creation, username)
                        VALUES('{self.__hash}', '{self.__date}', '{username}')""")
        conn.disconnect()