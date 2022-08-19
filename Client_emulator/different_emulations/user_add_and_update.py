import re

from Client_emulator.emulate_functions import db_register, db_login, upgrade_vocabulary

if __name__ == '__main__':
    username = 'Piterson'
    password = 'admin12345'
    cookie = db_login(username, password)
    with open(r"C:\Users\Neptune\Desktop\text.txt", "r") as file:
        content = file.read()
        pattern = r"[a-zA-Z]+"
        res_list = re.findall(pattern, content)
        # upgrade_vocabulary(cookie, username, res_list)