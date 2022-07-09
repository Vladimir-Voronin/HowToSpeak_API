class UserEntity:
    def __init__(self, id, name, salt, hash_password):
        self.id = id
        self.name = name
        self.salt = salt
        self.hash_password = hash_password
