class TooManyPlayersException(BaseException):
    default_message = "В игре не может быть больше 6 игроков"
   
    def __init__(self, message=None):
        super().__init__(message or self.default_message)
