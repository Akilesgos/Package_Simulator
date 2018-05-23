from random import randint

class Package:
    def __init__(self) -> str:  # Сохранить название сплетни
        self.name = ''.join([(chr(randint(97, 122))) for x in range(10)])