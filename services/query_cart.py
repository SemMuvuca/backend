from database.firestore import get_product


async def query_cart(order_list):
    product_obj = {"total_price": 0.0, "total_weight": 0.0}
    for item in order_list["products_quantity"]:
        product_data = await get_product(item["ean13_code"])
        product_obj["total_price"] += product_data["unit_price"] * item["quantity"]
        product_obj["total_weight"] += product_data["weight"] * item["quantity"]
    return product_obj
