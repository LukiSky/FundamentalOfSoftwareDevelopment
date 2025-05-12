class LoginError(ValueError):
    pass

class ValidationError(ValueError):
    def __init__(self, message="Incorrect email or password format"):
        super().__init__(message)