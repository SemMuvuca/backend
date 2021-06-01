from google.cloud import datastore

client = datastore.Client()


def create_key(ean13_code: str):
    return client.key("Produto", ean13_code)


def create_multi_key_list(ean13_code):
    return [create_key(item) for item in ean13_code]


def get_product(ean13_code: str):
    return client.get(key=create_key(ean13_code))


def get_multi_product(checkout_list: list):
    return client.get_multi(checkout_list)
