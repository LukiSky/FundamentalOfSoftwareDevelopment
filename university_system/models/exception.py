### Color Controls ###

RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

####

class LoginError(ValueError):
    pass

class ValidationError(ValueError):
    def __init__(self, message= RED + "Incorrect email or password formats" + RESET):
        super().__init__(message)