from enum import Enum


class ModelName(str, Enum):
    mercado_pago = "mercado_pago"
    picpay = "picpay"
    stripe = "stripe"
