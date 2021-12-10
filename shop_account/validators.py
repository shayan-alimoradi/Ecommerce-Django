from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.isnumeric():
        raise ValidationError("Phone number must be numeric")
