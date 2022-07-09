from APIServer.Cashing.DB_Entities.user import UserEntity
from HTSDatabase.db_response import DBresponce


class ReadDB:
    @staticmethod
    def is_user_existent_by_name(db, name):
        col = db['users']
        if len(list(col.find({'name': name}))) != 0:
            return True
        return False

    @staticmethod
    def user_info_by_name(db, name):
        col = db['users']
        user = col.find_one({'name': name})
        if len(list(user)) == 0:
            return DBresponce(False, 'There is no user with this name')

        user_ent = UserEntity(user['_id'], user['name'], user['salt'], user['hash_password'])
        db_responce = DBresponce(True)
        db_responce.info = {'User_entity': user_ent}

        return db_responce


