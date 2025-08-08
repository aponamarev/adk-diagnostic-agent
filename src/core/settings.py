"""Settings for the diagnostic agent."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the diagnostic agent."""

    # Set environment variable prefix for the settings.
    model_config = {"env_prefix": "DIAGNOSTIC_"}

    model_name: str = "gemini-2.0-flash"
    model_temperature: float = 0.01
    diagnostic_field: str = "diagnostic_information"
    extracted_information_field: str = "extracted_information"
    missing_information_field: str = "missing_information"


diagnostic_settings = Settings()
