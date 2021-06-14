from application import _carrinho_list
from application import _produto_list
from application.model.entity.produto import Produto
import json

class ProdutoDAO:

    def __init__(self):
        self.carrinho_list = _carrinho_list
        self.produto_list = _produto_list

    def mostrar_carrinho(self):
        return self.carrinho_list

    def mostrar_produto(self):
        return self.produto_list

    def dict_to_list(self, json):
        list = []
        for product in json:
            produto = Produto()
            price = product["price"]
            produto.set_id(product["id"])
            produto.set_nome(product["name"])
            produto.set_img(product["images"])
            produto.set_valor(price["value"])
            produto.set_parcela(price["installments"])
            produto.set_valor_parcela(price["installmentValue"])
            list.append(produto)
        return list

    def listar_todos(self):
        resultado = []
        with open("application/json/buscape.json", "r") as file:
            _produto_list = json.load(file)
            resultado = self.dict_to_list(_produto_list)
        return resultado