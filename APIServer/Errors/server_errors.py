from flask import jsonify

from APIServer.__init__ import app


@app.errorhandler(404)
def resource_not_found(e):
    if e.data is not None:
        return jsonify(error=str(e.data['description'])), 404
    return jsonify(error='Error 404'), 404


@app.errorhandler(403)
def resource_not_found(e):
    if e.data is not None:
        return jsonify(error=str(e.data['description'])), 403
    return jsonify(error='Error 403'), 403


@app.errorhandler(400)
def resource_not_found(e):
    if e.data is not None:
        return jsonify(error=str(e.data['description'])), 400
    return jsonify(error='Error 400'), 400
