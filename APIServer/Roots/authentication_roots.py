from flask import request, jsonify
from APIServer.Errors.validation_errors import request_validation
from APIServer.Main.user import User
from APIServer.__init__ import app, BASE_URL, DB, CasherHTS
from flask_restful import abort
from HTSDatabase.ReadAPI.hts_db_read import ReadDB
from HTSDatabase.WriteAPI.hts_db_write import WriteDB
from flask import session


@app.route(BASE_URL + '/set/')
def set():
    session['key'] = 'value'
    return 'ok'


@app.route(BASE_URL + '/get/')
def get():
    return session.get('key', 'not set')


@app.route(BASE_URL + '/login', methods=['POST'])
def login():
    request_data = request.get_json()
    request_validation(request_data, 'username', 'password')
    name = request_data['username']
    password = request_data['password']

    # cashing
    if name in CasherHTS.users_bname:
        user_entity = CasherHTS.users_bname[name]
    else:
        if not ReadDB.is_user_existent_by_name(DB, name):
            abort(403, description=f"User with this nickname are not existed")

        db_resp = ReadDB.user_info_by_name(DB, name)
        if not db_resp:
            abort(403, description=f"DB Error")
        user_entity = db_resp.info['User_entity']
        CasherHTS.users_bname[name] = user_entity
    is_valid = User().is_valid_user(user_entity.salt, user_entity.hash_password, password)
    if is_valid:
        session[name] = name
        return jsonify(text='Your are logged in')
    else:
        abort(403, description=f"Username or password are not valid")


@app.route(BASE_URL + '/register', methods=['POST'])
def register():
    request_data = request.get_json()
    request_validation(request_data, 'username', 'password')
    name = request_data['username']
    password = request_data['password']
    if ReadDB.is_user_existent_by_name(DB, name):
        abort(403, description="User with this username already exists")
    user = User().register(name, password)

    db_r = WriteDB.register_user(DB, user)
    if not db_r.ok:
        abort(403, description=f"DB Error")

    return jsonify(text='Your have been registred, use your username to get access for this API')
