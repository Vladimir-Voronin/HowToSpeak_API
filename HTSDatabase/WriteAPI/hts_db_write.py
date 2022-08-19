from APIServer.Cashing.DB_Entities.word import WordEntity
from HTSDatabase.ReadAPI.hts_db_read import ReadDB
from HTSDatabase.db_response import DBresponse


class WriteDB:
    @staticmethod
    def register_user(db, user):
        col = db['users']
        if not ReadDB.is_user_existent_by_name(db, user.username):
            col.insert_one(
                {'name': user.username, 'salt': user.salt, 'hash_password': user.hash_password, 'words_list': []})
            return DBresponse(True)

        return DBresponse(False, 'DB Error')

    @staticmethod
    def update_user_vocabulary(db, username, freq_dict, words=None):
        if not freq_dict:
            return DBresponse(True, 'there are no such words in DB')

        col_users = db['users']

        user_list = col_users.find({'name': username})
        current_values = {}
        user_already_used = user_list[0]['words_list']
        for i in user_already_used:
            current_values[i['text']] = i['frequencyUse']

        for k, v in freq_dict.items():
            if k in current_values:
                current_values[k] += v
            else:
                current_values[k] = v

        result = []
        for k, v in current_values.items():
            result.append({'text': k, 'frequencyUse': v})

        col_users.update_one({'name': username}, {'$set': {'words_list': result}})
        return DBresponse(True)
