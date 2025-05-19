class LoginError(ValueError):
    pass

class ValidationError(ValueError):
    def __init__(self, message= "Incorrect email or password formats"):
        super().__init__(message)