from tortoise.expressions import RawSQL


class CosineSimilarity(RawSQL):
    def __init__(self, field: str, vector: list[float], vector_size: int = 1536):
        super().__init__(
            f"public.COSINE_DISTANCE({field}, "
            f"public.array_to_vector(ARRAY{vector}, {vector_size}, true))"
        )
