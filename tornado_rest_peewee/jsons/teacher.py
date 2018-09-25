from jsonschema import ValidationError, SchemaError, FormatChecker
from .defaultvalidator import DefaultDraft4Validator

create = {
    "type": "object",
    "properties": {
        "teacher_id": {"type": "number"},
        "name": {"type": "string", "default": "名字"},
        "description": {"type": "string"},
        "created_by": {"type": "string"},
        "created": {"type": "string", "format": "date-time"},
        "modified_by": {"type": "string"},
        "modified": {"type": "string", "format": "date-time"},
    },
    "required": [
        "teacher_id",
    ],
    "additionalProperties": False,
}

update = {
    "type": "object",
    "properties": {
        "teacher_id": {"type": "number"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "created_by": {"type": "string"},
        "created": {"type": "string", "format": "date-time"},
        "modified_by": {"type": "string"},
        "modified": {"type": "string", "format": "date-time"},
    },
    "required": [
    ],
    "additionalProperties": False,
}


class TeacherSchema(object):
    _id = str

    def validator(self, data, schema='create'):
        try:
            DefaultDraft4Validator(
                globals()[schema], format_checker=FormatChecker()).validate(data)
        except ValidationError as e:
            return e.message
        except SchemaError as e:
            return e
        return None
