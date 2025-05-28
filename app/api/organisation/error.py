class OrganizationError(Exception):
    """Base class for organization-related errors."""

    pass


class OrganizationAlreadyExistsError(OrganizationError):
    """Raised when the organization name is already registered."""

    def __init__(self, name: str):
        super().__init__(f"Organization '{name}' is already registered.")


class OrganizationNotFoundError(OrganizationError):
    """Raised when the organization is not found."""

    def __init__(self, name: str):
        super().__init__(f"Organization '{name}' not found.")


class MigrationPendingError(OrganizationError):
    """Raised when the DB schema is not up-to-date."""

    def __init__(self):
        super().__init__("Database is not up-to-date. Please run migrations.")


class AdminUserCreationError(OrganizationError):
    """Raised when admin user creation fails."""

    def __init__(self, schema: str, original_exception: Exception):
        super().__init__(
            f"Failed to create admin user in schema '{schema}': {original_exception}"
        )
