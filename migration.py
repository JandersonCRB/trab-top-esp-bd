import pymongo


def migrate(client):
    client.products.create_index([('name', pymongo.ASCENDING),
                               ('product_id', pymongo.ASCENDING)], unique=True)
