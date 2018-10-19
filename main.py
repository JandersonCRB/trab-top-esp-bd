import xml.etree.ElementTree as ET
import pymongo
from User import User
import migration

def products_dict(db):
    tree      = ET.parse("./DB/products.xml")
    root      = tree.getroot()
    products  = root.findall('product')
    product_list = []
    _id = 0
    for product in products:
        try:
            description = product.find('description').text
            SellPriceMax = product.find('SellPriceMax').text
            SellPriceMin = product.find('SellPriceMin').text
            razaoSocialName = product.find('razaoSocialName').text
            # razaoSocialKey = db.stores.find_one({'razaoSocialName': razaoSocialName})["_id"]
            product_list.append({ 'id'            : _id,
                                 'description'    : description,
                                 'SellPriceMax'   : SellPriceMax,
                                 'SellPriceMin'   : SellPriceMin,
                                 'razaoSocialKey' : razaoSocialName})
            _id = _id + 1
        except:
            pass
        

    return product_list


def stores_dict():
    tree = ET.parse('./DB/products.xml')
    root = tree.getroot()
    stores = {}
    for product in root.findall('product'):
        try:
            razaoSocialName = product.find('razaoSocialName').text
            fantasiaName = product.find('fantasiaName').text
            neighborhood = product.find('neighborhood').text
            cepNum = product.find('cepNum').text
            cityName = product.find('cityName').text
            SellPriceMax = product.find('SellPriceMax').text
            SellPriceMin = product.find('SellPriceMin').text
            longitudeNum = product.find('longitudeNum').text
            store_obj = {'razaoSocialName': razaoSocialName,
                         'fantasiaName': fantasiaName,
                         'neighborhood': neighborhood,
                         'cepNum': cepNum,
                         'cityName': cityName,
                         'SellPriceMax': SellPriceMax,
                         'SellPriceMin': SellPriceMin,
                         'latitudeNum': longitudeNum}
            stores[razaoSocialName] = store_obj
        except:
            pass
    return stores.values()


def save_stores_to_mongo(db):
    stores = db.stores
    try:
        stores.insert_many(stores_dict())
    except pymongo.errors.BulkWriteError:
        print("Tentativa de salvar objeto com chave duplicada no mongoDB.")


def main():
    client = pymongo.MongoClient(
        "mongodb://mongo:mongol@trab-top-esp-bd-shard-00-00-3bzqm.mongodb.net:27017,trab-top-esp-bd-shard-00-01-3bzqm.mongodb.net:27017,trab-top-esp-bd-shard-00-02-3bzqm.mongodb.net:27017/test?ssl=true&replicaSet=trab-top-esp-bd-shard-0&authSource=admin&retryWrites=true")
    migration.migrate(client.test)
    user = User('Marcus', client.test)
    user.favorite_product('2222')


if __name__ == "__main__":
    main()
