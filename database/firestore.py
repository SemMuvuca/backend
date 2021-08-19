from google.cloud import firestore

db = firestore.AsyncClient(project="sem-muvuca-323320")


# async def create_key(ean13_code: str):
#    return client.key("Produto", ean13_code)


# async def create_multi_key_list(ean13_code):
#    return [create_key(item) for item in ean13_code]


async def get_product(ean13_code: str):
    return await db.collection("products").document(ean13_code).get().to_dict()


# async def get_multi_product(checkout_list: list):
#    return client.get_multi(checkout_list)
