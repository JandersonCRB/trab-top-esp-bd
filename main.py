# coding=utf-8
import xml.etree.ElementTree as ET
import sys
from User import User
import migration
import pymongo
import product_search

right_price_logo = "###################################################################################\n############                        RIGHT$PRICE                        ############\n###################################################################################"

try: input = raw_input
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
    answer = None
    while answer != 'voltar':
        product_dict = search_id_list(user.buy_list())
        print("################################################# LISTA DE COMPRAS ####################################################\n")
        if not product_dict:
            print ("Você nao tem nenhum produto na sua Lista de Compras.\n")
            break
        for product in product_dict:
            print ("\n\n###################################################################################")
            print (product['id'] + ' - ' + product['description'])
            print ('Valor maximo: ' + product['SellPriceMax'])
            print ('Valor minimo: ' + product['SellPriceMin'])
            print (product['razaoSocialName'])
            print (product['addressName'] + ', ' + product['neighborhood'])
            print ("###################################################################################")


        print("Deseja deletar algum produto da sua Lista de Compras?      Digite o ID do produto ou 'voltar' se nao desejar")
        answer = raw_input()
        if answer != 'voltar':
            user.unfavorite_product(answer)



def search_product_menu(user):
    sys.stdout.flush()
    print(right_price_logo)
    print("\n\n")

    print("Digite o nome do produto:\n")
    product_name = raw_input()
    products_list = product_search.product_search(product_name, limit=20)
    i = 0
    for product in products_list:
        print(str(i) + ' - ' + product['name'])
        i += 1
    print("\nDigite o codigo do produto que deseja adicionar a sua lista de compras:")
    product_id = int(raw_input())

    try:
        user.favorite_product(products_list[product_id]['id'])
        print("Produto " + str(product_id) + " adicionado com sucesso!\n")

    except pymongo.errors.DuplicateKeyError:
        print("Voce ja possui este produto adicionado em sua lista.")


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
    # user.favorite_product('48214')
    while exit_program is False:
        print("Bem-vindo, " + user.name + '!\n')
        print("O que deseja fazer?\n\n"
              "1) Procurar produto\n"
              "2) Lista de Compras\n"
              "3) Sair")
        resposta = raw_input()

        if resposta == '1':
            search_product_menu(user)
        if resposta == '2':
            shop_list_menu(user)
        if resposta == '3':
            print("\nAte mais, " + nome + '!')
            exit_program = True

if __name__ == "__main__":
    main()

