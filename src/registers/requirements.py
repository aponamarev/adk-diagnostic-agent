"""Simple registry and missing-information collector for session state.

Minimal rules:
- RequirementsRegistry.register(model) only accepts a Pydantic model class.
- Duplicate registrations by normalized name raise RegistryModelAlreadyExistsError.
- get_required_fields() returns a set of keys in the form "model_name:field"
  (snake_case for both name and field).
- collect_missing_information(ctx, registry) simply checks if each required
  key exists in ctx.state. If a key is absent, it is considered missing.
"""

import re

from google.adk.sessions.state import State
from pydantic import BaseModel

from core.diagnostic_types.chief_complaint import ChiefComplaintType
from core.exceptions import RegistryModelAlreadyExistsError
from core.settings import diagnostic_settings


def _snake_case(name: str) -> str:
    """Convert CamelCase or mixed names to snake_case; strip trailing _type."""
    # Insert underscore before uppercase letters that follow lowercase letters
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    return snake


class RequirementsRegistry:
    """Minimal registry for Pydantic models used in diagnostic collection."""

    _models: dict[str, type[BaseModel]] = {}

    @classmethod
    def register(cls, model: type[BaseModel]) -> None:
        """Register a Pydantic model by its normalized name.

        Args:
            model: The Pydantic model class to register.
        """
        name = _snake_case(model.__name__)
        if name in cls._models:
            raise RegistryModelAlreadyExistsError(name)
        cls._models[name] = model

    @classmethod
    def get_required_fields(cls) -> set[str]:
        """Return required fields as "model_name:field" in snake_case.

        All model fields are considered required in this simple version.
        """
        required: set[str] = set()
        for model_name, model in cls._models.items():
            for field_name in model.model_fields.keys():
                required.add(f"{model_name}:{_snake_case(field_name)}")
        return required


def collect_missing_information(
    state: State,
) -> set[str]:
    """Return required keys that are absent from ctx.state (existence check only)."""
    required_keys = RequirementsRegistry.get_required_fields()
    missing_keys = set()
    for key in required_keys:
        if f"{diagnostic_settings.diagnostic_field}:{key}" not in state:
            missing_keys.add(key)
    return missing_keys


__all__ = [
    "RequirementsRegistry",
    "collect_missing_information",
]


# Register all models that define required diagnostic information
RequirementsRegistry.register(ChiefComplaintType)
