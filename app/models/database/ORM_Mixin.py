from tortoise import fields


class TimestampMixin:
    created_at = fields.DatetimeField(
        null=True,
        auto_now_add=True,
        description="Creation date on the database",
    )
    modified_at = fields.DatetimeField(
        null=True,
        auto_now=True,
        description="Last change registraded on the database",
    )
