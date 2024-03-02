class BaseDBException(Exception):
    def __init__(self, details: str):
        self.reason = "Unknown"
        self.details = details


class DBUniqueException(BaseDBException):
    def __init__(self, details: str):
        self.reason = "Данные не уникальны."
        self.details = details

class DoesNotExistsException(BaseDBException):
    def __init__(self, reason: str, details: str):
        self.reason = reason
        self.details = details

class CountryDoesNotExists(DoesNotExistsException):
    def __init__(self):
        self.reason = "Страна с указанным кодом не найдена."
        self.details = "None"


class UserDoesNotExists(DoesNotExistsException):
    def __init__(self):
        self.reason = "Пользователь с данным логином не найден."
        self.details = "None"