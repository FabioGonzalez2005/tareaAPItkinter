import requests
from models.api_response import APIResponse
from dataclass_wizard import fromdict
from vista import interfaz

def main():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)
    print(interfaz.mostrarProductos(product_list))

if __name__ == "__main__":
    main()



