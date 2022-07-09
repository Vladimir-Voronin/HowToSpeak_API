class DBresponse:
    def __init__(self, ok: bool, message=''):
        self.ok = ok
        self.message = message
        self.info = None
