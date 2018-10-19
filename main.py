import xml.etree.ElementTree as ET
import sys
from User import User
import migration
import pymongo

right_price_logo = "###################################################################################\n############                        RIGHT$PRICE                        ############\n###################################################################################"

try: raw_input = input
except NameError: pass

def products_dict():
    tree      = ET.parse("./DB/products.xml")
    root      = tree.getroot()
    products  = root.findall('product')
    product_dict = {}

    for product in products:
        id = product.find('id').text
        description = product.find('description').text
        SellPriceMax = product.find('SellPriceMax').text
        SellPriceMin = product.find('SellPriceMin').text

        product_dict[id] = { 'id'           : id,
                             'description'  : description,
                             'SellPriceMax' : SellPriceMax,
                             'SellPriceMin' : SellPriceMin}

    return product_dict

def stores_dict():
    tree = ET.parse('./DB/products.xml')
    root = tree.getroot()

    stores = {}
    for product in root.findall('product'):
        node = product.find('razaoSocialName')
        if node is not None:
            razaoSocialName = node.text
            fantasiaName = product.find('fantasiaName').text
            neighborhood = product.find('neighborhood').text
            cepNum = product.find('cepNum').text
            cityName = product.find('cityName').text
            SellPriceMax = product.find('SellPriceMax').text
            SellPriceMin = product.find('SellPriceMin').text
            longitudeNum = product.find('longitudeNum').text
            stores[razaoSocialName] = {'razaoSocialName': razaoSocialName,
                                         'fantasiaName': fantasiaName,
                                         'neighborhood': neighborhood,
                                         'cepNum': cepNum,
                                         'cityName': cityName,
                                         'SellPriceMax': SellPriceMax,
                                         'SellPriceMin': SellPriceMin,
                                         'latitudeNum': longitudeNum}
    return stores


def search_id_list(id_list):
    result_list = []
    tree = ET.parse("./DB/products.xml")
    root = tree.getroot()
    for product_id in id_list:
        product = root.find('product[id=\''+product_id+'\']')
        id = product.find('id')
        if id is not None:
            id = id.text
        description = product.find('description')
        if description is not None:
            description = description.text

        SellPriceMax = product.find('SellPriceMax')
        if SellPriceMax is not None:
            SellPriceMax = SellPriceMax.text

        SellPriceMin = product.find('SellPriceMin')
        if SellPriceMin is not None:
            SellPriceMin = SellPriceMin.text

        addressName = product.find('addressName')
        if addressName is not None:
            addressName = addressName.text

        razaoSocialName = product.find('razaoSocialName')
        if razaoSocialName is not None:
            razaoSocialName = razaoSocialName.text

        neighborhood = product.find('neighborhood')
        if neighborhood is not None:
            neighborhood = neighborhood.text
        result_list.append({'id'              : id,
                            'description'     : description,
                            'SellPriceMax'    : SellPriceMax,
                            'SellPriceMin'    : SellPriceMin,
                            'addressName'     : addressName,
                            'razaoSocialName' : razaoSocialName,
                            'neighborhood'    : neighborhood
                            })
    return result_list


def shop_list_menu(user):
    print(search_id_list(user.buy_list()))


def search_product(name):
    product_list = ["1 - Rola de " + name, "2 - Pica de " + name, "3 - Buceta de " + name,
                    "4 - Sua Mae de " + name, "5 - Minha vo de " + name, "6 - Ta no face " + name]
    return (product_list)


def add_product_to_shop_list(product_id):
    print(product_id + " adicionado com sucesso!")


def search_product_menu():
    sys.stdout.flush()
    print(right_price_logo)
    print("\n\n")

    print("Digite o nome do produto:\n")
    product_name = raw_input()
    products_list = search_product(product_name)
    for product in products_list:
        print(product)
    print("\nDigite o codigo do produto que deseja adicionar a sua lista de compras:")
    product_id = raw_input()
    add_product_to_shop_list(product_id)


def intro_menu():
    sys.stdout.flush()
    print(right_price_logo)
    print("\n\n")
    print("Qual seu nome?")

    nome = raw_input()

    return nome

def main():
    client = pymongo.MongoClient("mongodb://mongo:mongol@trab-top-esp-bd-shard-00-00-3bzqm.mongodb.net:27017,trab-top-esp-bd-shard-00-01-3bzqm.mongodb.net:27017,trab-top-esp-bd-shard-00-02-3bzqm.mongodb.net:27017/test?ssl=true&replicaSet=trab-top-esp-bd-shard-0&authSource=admin&retryWrites=true")
    migration.migrate(client.test)

    # user = User('Marcus', client.test)
    # try:
    #     user.favorite_product('2233')
    # except pymongo.errors.DuplicateKeyError:
    #     print("Voc j possui este produto adicionado em sua lista.")
    # print(user.buy_list())

    exit_program = False
    nome = intro_menu()
    user = User(nome, client.test)
    while exit_program is False:
        print("Bem-vindo, " + user.name + '!\n')
        print("O que deseja fazer?\n\n"
              "1) Procurar produto\n"
              "2) Lista de Compras\n"
              "3) Sair")
        resposta = raw_input()

        if resposta == '1':
            search_product_menu()
        if resposta == '2':
            shop_list_menu(user)
        if resposta == '3':
            print("\nAte mais, " + nome + '!')
            exit_program = True

if __name__ == "__main__":
    main()

