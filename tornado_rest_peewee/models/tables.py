from peewee import (
    CharField,
    IntegerField,
)

from .base import BaseModel


class Teacher(BaseModel):

    name = CharField()
    teacher_id = IntegerField(unique=True)
