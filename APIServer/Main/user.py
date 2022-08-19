import secrets

import bcrypt

from APIServer.config import SALT_PASSWORD_GENERAL


class User:
    def __init__(self):
        self.username = None
        self.salt = None
        self.hash_password = None

    def register(self, name: str, password: str):
        password = bytes(password.encode('utf-8'))
        self.salt = bcrypt.gensalt()
        self.username = name
        password = password + SALT_PASSWORD_GENERAL
        self.hash_password = bcrypt.hashpw(password, self.salt).decode('utf-8')
        self.salt = self.salt.decode('utf-8')
        return self

    @staticmethod
    def is_valid_user(db_salt, db_password, password):
        db_salt = bytes(db_salt.encode('utf-8'))
        db_password = bytes(db_password.encode('utf-8'))
        password = bytes(password.encode('utf-8')) + SALT_PASSWORD_GENERAL
        if db_password == bcrypt.hashpw(password, db_salt):
            return True
        return False
