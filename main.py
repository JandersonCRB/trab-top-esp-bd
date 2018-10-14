import xml.etree.ElementTree as ET


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


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
