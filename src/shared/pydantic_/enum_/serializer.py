from pydantic import PlainSerializer


EnumNameSerializer = PlainSerializer(
    lambda e: e.name,
    when_used='always',
)
