import mercadopago

# from database.firestore import get_product
sdk = mercadopago.SDK("")


async def status_order(data):
    data["transaction_amount"] = data["transactionAmount"]
    data.pop("transactionAmount")
    data["issuer_id"] = data["issuerId"]
    data.pop("issuerId")
    data["payment_method_id"] = data["paymentMethodId"]
    data.pop("paymentMethodId")
    payment_response = sdk.payment().create(data)
    return payment_response["response"]
