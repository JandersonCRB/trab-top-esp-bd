
class User:

    def __init__(self, name, db):
        self.name = name
        self.db = db

    def favorite_product(self, product_id):
        return self.db.products.insert_one({'name': self.name, 'product_id': product_id}).inserted_id

    def buy_list(self):
        return self.db.products.find({'name': self.name})
