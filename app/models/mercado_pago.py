from typing import Optional
from typing_extensions import TypedDict
from pydantic import BaseModel, EmailStr, condecimal


class _identification(TypedDict):
    type: str
    number: str


class _payer(TypedDict):
    email: EmailStr


class client_payment_data(TypedDict):
    token: str
    issuerId: str
    description: str
    transactionAmount: int
    installments: int
    paymentMethodId: str
    payer: _payer


class server_payment_data(BaseModel):
    token: str
    issuer_id: str
    description: str
    transaction_amount: int
    installments: int
    payment_method_id: str
    payer: _payer
