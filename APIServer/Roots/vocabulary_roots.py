from flask import request, jsonify
from pyhts.hts_natural_language.text_analysis import TextAnalysis

from APIServer.Errors.validation_errors import request_validation
from APIServer.Main.user import User
from APIServer.__init__ import app, BASE_URL, DB, CasherHTS
from flask_restful import abort
from HTSDatabase.ReadAPI.hts_db_read import ReadDB
from HTSDatabase.WriteAPI.hts_db_write import WriteDB
from flask import Flask, session


@app.route(BASE_URL + '/update/vocabulary', methods=['POST'])
def update_vocabulary():
    request_data = request.get_json()
    request_validation(request_data, 'username', 'words')
    name = request_data['username']

    if name not in session:
        abort(403, description=f"You are not logged in")

    words = request_data['words']

    freq_dict = TextAnalysis.get_frequency_by_list(words)
    WriteDB.update_user_vocabulary(DB, name, freq_dict)
    return jsonify(text='Your vocabulary has been updated')
