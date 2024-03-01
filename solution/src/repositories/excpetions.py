class BaseDBException(Exception):
    def __init__(self, details: str):
        self.reason = "Unknown"
        self.details = details


class DBUniqueException(BaseDBException):
    def __init__(self, details: str):
        self.reason = "Данные не уникальны."
        self.details = details

class CountryDoesNotExists(BaseDBException):
    def __init__(self):
        self.reason = "Страна с указанным кодом не найдена."
        self.details = "None"
