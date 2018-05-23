from random import randint


class Package:
    """Create Package"""

    def __init__(self) -> 'str':
        self.name = ''.join([(chr(randint(97, 122))) for x in range(10)])
