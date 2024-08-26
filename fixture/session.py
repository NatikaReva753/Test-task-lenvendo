import os
import json


class SessionHelper:
    def __init__(self, wd):
        self.wd = wd

    def login(self):
        # Определяем абсолютный путь к файлу config.json
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')

        # Читаем данные для авторизации из config.json
        with open(config_path) as f:
            config = json.load(f)
            username = config['username']
            password = config['password']

        # Используем Basic авторизацию, добавляя логин и пароль к URL
        self.wd.get(f"http://{username}:{password}@qa.digift.ru/")