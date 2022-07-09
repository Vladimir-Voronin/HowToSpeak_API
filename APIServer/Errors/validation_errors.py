from typing import Optional, List

from flask_restful import abort


def request_validation(request_, *data):
    not_present = []
    for value in data:
        if value not in request_:
            not_present.append(value)

    if len(not_present) == 0:
        return True
    else:
        if len(not_present) == 1:
            info = "".join(not_present)
            abort(403, description=f"Please, add field {info} to your data")
        else:
            info = ", ".join(not_present)
            abort(403, description=f"Please, add field '{info}' to your data")
