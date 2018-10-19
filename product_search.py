import xml.etree.ElementTree as ET

def product_search(search, limit=10):
    tree      = ET.parse("./DB/products.xml")
    root      = tree.getroot()
    products = []
    for product in root.findall('product'):
        name = product.find('description').text
        print(name.upper(), search.upper())
        if name.upper().find(search.upper()) != -1:
            products.append({'id': product.find('id').text, 'name': product.find('description').text})
    return products[:limit]
