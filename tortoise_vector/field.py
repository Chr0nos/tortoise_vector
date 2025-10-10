from __future__ import annotations

from typing import Any

from tortoise.fields.base import Field
from tortoise.models import Model


class VectorField(Field, list):  # type:ignore
    """Defines a `vector` in postgres, this is needed to be able to
    use the vector extenssion since all the functions uses a vector
    instead of a float4[]
    """

    def __init__(self, vector_size: int, schema: str | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._vector_size = vector_size
        self._schema = schema or "public."

    @property
    def SQL_TYPE(self) -> str:  # type: ignore
        return f"{self._schema}vector({self._vector_size})"

    def to_db_value(self, value: list[float], instance: type[Model] | Model) -> str:
        if isinstance(value, list):
            return "[" + ",".join(map(str, value)) + "]"
        return value

    def to_python_value(self, value: Any) -> list[float]:
        if isinstance(value, str):
            value = value.removeprefix("[").removesuffix("]")
            return list(map(float, value.split(",")))
        return value
