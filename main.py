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
    pass


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
