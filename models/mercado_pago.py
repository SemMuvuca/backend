from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, EmailStr, condecimal


class _identification:
    type: str
    number: str


class _payer(BaseModel):
    email: str


#    identification: _identification


class client_payment_data(BaseModel):
    token: str
    issuerId: str
    description: str
    transactionAmount: int
    installments: int
    paymentMethodId: str
    payer = {"email": str}


class server_payment_data(BaseModel):
    token: str
    issuer_id: str
    description: str
    transaction_amount: int
    installments: int
    payment_method_id: str
    payer = {"email": str}
