from enum import Enum

from pydantic import BeforeValidator


def enum_name_validator(enum_class: type[Enum]) -> BeforeValidator:
    return BeforeValidator(
        lambda x: enum_class[x]
    )
