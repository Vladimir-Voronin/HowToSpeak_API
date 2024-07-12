import json

from flask import request, jsonify
from pyhts.hts_natural_language.text_analysis import TextAnalysis
from pyhts.hts_words_priority.priority_calculations import WordsPriorityCalculations

from APIServer.Errors.validation_errors import request_validation
from APIServer.Main.user import User
from APIServer.Main.words_priority_handling import Handler_methods_dict, WordsPriorityInput
from APIServer.__init__ import app, BASE_URL, DB, CasherHTS
from flask_restful import abort
from HTSDatabase.ReadAPI.hts_db_read import ReadDB
from HTSDatabase.WriteAPI.hts_db_write import WriteDB
from flask import Flask, session


@app.route(BASE_URL + '/vocabulary/update', methods=['POST'])
def update_vocabulary():
    request_data = request.get_json()
    request_validation(request_data, 'username', 'words')
    name = request_data['username']

    if name not in session:
        abort(403, description=f"You are not logged in")

    words = request_data['words']

    freq_dict = TextAnalysis.get_frequency_by_list(words)
    print(freq_dict)

    WriteDB.update_user_vocabulary(DB, name, freq_dict)
    return jsonify(text='Your vocabulary has been updated')


@app.route(BASE_URL + '/vocabulary/get', methods=['GET'])
def get_vocabulary():
    request_data = request.get_json()
    request_validation(request_data, 'username', 'frequency_method_name', 'number_of_words', 'handler_method')
    name = request_data['username']

    if name not in session:
        abort(403, description=f"You are not logged in")

    frequency_method_name = request_data['frequency_method_name']
    number_of_words = request_data['number_of_words']

    handler_method_name = request_data['handler_method']

    if handler_method_name not in Handler_methods_dict:
        abort(403, description=f"There no such handler method")

    handler_method = Handler_methods_dict[handler_method_name]

    freq_current_dict, method_type = ReadDB.get_method_frequency_dict(DB, frequency_method_name)
    user_dict = ReadDB.get_user_frequency_dict(DB, name)

    wpi_object = WordsPriorityInput(freq_current_dict, method_type, user_dict, number_of_words)

    words_list = handler_method(wpi_object)

    data = {'text': "You can get your words list by 'words_list'", 'words_list': words_list}
    json_data = json.dumps(data)

    return json_data
