"""Custom exceptions for the diagnostic agent."""


class RegistryModelAlreadyExistsError(KeyError):
    """Raised when attempting to register a model that already exists by name."""

    def __init__(self, model_name: str) -> None:
        super().__init__(f"Model already registered: '{model_name}'")
