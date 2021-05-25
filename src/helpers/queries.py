async def simple_query(db, entity: str, parameter: str, operation: str, value) -> list:

    query = db.query(kind=entity)
    query.add_filter(parameter, operation, value)
    consulta = list(query.fetch())
    return consulta[0]
