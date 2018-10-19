import xml.etree.ElementTree as ET
import sys
right_price_logo = "###################################################################################\n############                        RIGHT$PRICE                        ############\n###################################################################################"






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

def search_id_list(id_list):
    result_list = []
    tree = ET.parse("./DB/products.xml")
    root = tree.getroot()
    products = root.findall('product')
    for product_id in id_list:
        product = products.find('[id='+product_id+']')
        description = product['description']
        SellPriceMax = product['description']
        SellPriceMin = product['description']
        addressName = product['description']
        fantasiaName = product['description']
        neighborhood = product['description']
        result_list.append({'id'              : products.id,
                            'description'     : description,
                            'SellPriceMax'    : SellPriceMax,
                            'SellPriceMin'    : SellPriceMin,
                            'addressName'     : addressName,
                            'razaoSocialName' : fantasiaName,
                            'neighborhood'    : neighborhood
                            })

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

def shop_list_menu():
    pass

def search_product(name):
    product_list = ["1 - Rola de " + name, "2 - Pica de " + name, "3 - Buceta de " + name,
                    "4 - Sua Mae de " + name, "5 - Minha vo de " + name, "6 - Ta no face " + name]
    return product_list

def add_product_to_shop_list(product_id):
    print product_id + (" adicionado com sucesso!")


def search_product_menu():
    sys.stdout.flush()
    print right_price_logo
    print("\n\n")

    print("Digite o nome do produto:\n")
    product_name = raw_input()
    products_list = search_product(product_name)
    for product in products_list:
        print product
    print("\nDigite o codigo do produto que deseja adicionar a sua lista de compras:")
    product_id = raw_input()
    add_product_to_shop_list(product_id)

def intro_menu():
    sys.stdout.flush()
    print right_price_logo
    print("\n\n")
    print("Qual seu nome?")

    nome = raw_input()

    return nome

def main():
    logged_off = True
    exit_program = False
    while exit_program is False:
        if logged_off is True:
            nome = intro_menu()
        logged_off = False
        print("Bem-vindo, ") + nome + '!\n'
        print("O que deseja fazer?\n\n"
              "1) Procurar produto\n"
              "2) Lista de Compras\n"
              "3) Sair")
        resposta = raw_input()

        if resposta == '1':
            search_product_menu()
        if resposta == '2':
            shop_list_menu()
        if resposta == '3':
            print "\nAte mais, " + nome + '!'
            exit_program = True

if __name__ == "__main__":
    main()
