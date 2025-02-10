from typing import Any, Type

from tortoise import fields
from tortoise.models import Model


class VectorField(fields.Field, list):
    """Defines a `vector` in postgres, this is needed to be able to
    use the vector extenssion since all the functions uses a vector
    instead of a float4[]
    """

    def __init__(
        self,
        vector_size: int,
        schema: str | None = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._vector_size = vector_size
        self._schema = schema or "public."

    @property
    def SQL_TYPE(self) -> str:
        return f"{self._schema}vector({self._vector_size})"

    def to_db_value(self, value: list[float], instance: Type[Model] | Model) -> str:
        if isinstance(value, list):
            return "[" + ",".join([str(item) for item in value]) + "]"
        return value

    def to_python_value(self, value: Any) -> list[float]:
        if isinstance(value, str):
            value = value.removeprefix("[").removesuffix("]")
            return list([float(item) for item in value.split(",")])
        return value
