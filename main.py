import requests
from models.api_response import APIResponse
from dataclass_wizard import fromdict

def sacarElementoDeAPI():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)

# Imprimir el primer producto
print("Producto 0 (title): ", product_list.products[0].title)

# Imprimimos el atributo total
print("Total_str: ", product_list.total)

# Imprimir todos los titles
print()
for product in product_list.products:
    print(product.title)


