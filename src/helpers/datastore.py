from google.cloud import datastore

client = datastore.Client()


async def single_query(entity: str, parameter: str, value) -> list:
    query = client.query(kind=entity)
    query.add_filter(parameter, "=", value)
    consulta = list(query.fetch())
    return consulta[0]
