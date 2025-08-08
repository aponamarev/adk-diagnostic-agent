from typing import Any, Self

from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base class for all diagnostic types."""

    @classmethod
    def flatten_names(cls) -> list:
        """Return all field names in a flattened fashion, with nested models concatenated using ':'."""
        flattened = []

        for field_name, field_info in cls.model_fields.items():
            field_type = field_info.annotation

            if isinstance(field_type, type) and issubclass(field_type, BaseSchema):
                child_fields = field_type.flatten_names()
                flattened.extend(
                    [f"{field_name}:{child_field}" for child_field in child_fields]
                )
            else:
                flattened.append(field_name)

        return flattened

    def update(self, update_dict: dict[str, Any]) -> Self:
        """Deep update a model instance with a dictionary using a recursive approach."""
        updated_model = self.model_copy(deep=True)
        for key, value in update_dict.items():
            if value is None:
                continue

            field = getattr(updated_model, key, None)
            match field:
                case BaseSchema():
                    if isinstance(value, dict):
                        setattr(updated_model, key, field.update(value))
                    else:
                        setattr(updated_model, key, value)
                case _:
                    setattr(updated_model, key, value)
        return updated_model
