from models.database.ORM_Mixin import TimestampMixin
from tortoise import fields
from tortoise.models import Model


class Item(TimestampMixin, Model):
    id = fields.BigIntField(pk=True, null=False, description="EAN13 code")
    product_name = fields.TextField(null=False, description="Name of the product")
    quantity = fields.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        description="Volume or weight value",
    )
