import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number", "minimum": 18},
    },
    "required": ["name", "age"]
}

data = {"name": "Kamil", "age": 19}

try:
    validate(instance=data, schema=schema)
    print("Validation passed")
except ValidationError as e:
    print(f"Validation failed: {e}")