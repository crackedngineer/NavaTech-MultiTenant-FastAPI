class AuthenticationError(Exception):
    """Raised when authentication fails."""
    def __init__(self):
        super().__init__("Incorrect email or password.")
