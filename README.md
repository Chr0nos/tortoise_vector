# Implementation of vector from Tortoise-ORM
Usage:

```python
from tortoise_vector.field import VectorField
from tortoise_vector.expressions import CosineSimilarity
from tortoise import Model


OPENAI_VECTOR_SIZE = 1536


class MyModel(Model):
    # vectors have a fixed size, openai uses 1536 dimensions
    embedding = VectorField(vector_size=OPENAI_VECTOR_SIZE)



async def get_embedding_from_text(str: str) -> list[float]:
    ...


async def get_nearst_models(text: str) -> Queryset[MyModel]:
    embedding = await get_embedding_from_text(text)
    return (
        MyModel
        .all()
        .annotate(
            distance=CosineSimilarity(
                "embedding",
                embedding,
                OPENAI_VECTOR_SIZE
            )
        )
        .order_by("distance")
    )
```

