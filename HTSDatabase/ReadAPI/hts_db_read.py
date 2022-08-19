from APIServer.Cashing.DB_Entities.user import UserEntity
from HTSDatabase.db_response import DBresponse


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
            return DBresponse(False, 'There is no user with this name')

        user_ent = UserEntity(user['_id'], user['name'], user['salt'], user['hash_password'])
        db_responce = DBresponse(True)
        db_responce.info = {'User_entity': user_ent}

        return db_responce

    @staticmethod
    def get_method_frequency_dict(db, frequency_method_name):
        col_freq_method = db['frequencyMethods']
        words = col_freq_method.find({'name': frequency_method_name})
        words_list = list(words)

        words_dict_list = words_list[0]['wordsRatingList']
        type_ = words_list[0]['type']

        result_words = {}
        for d in words_dict_list:
            result_words[d['text']] = d['rating']

        return result_words, type_

    @staticmethod
    def get_user_frequency_dict(db, username):
        col_users = db['users']
        user_cursor = col_users.find({'name': username})

        user_dict_list = user_cursor[0]['words_list']

        result_user_dict = {}
        for d in user_dict_list:
            result_user_dict[d['text']] = d['frequencyUse']

        return result_user_dict
