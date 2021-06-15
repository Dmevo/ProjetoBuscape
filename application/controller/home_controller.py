from flask import render_template, url_for, request, jsonify
from application import app
from application.model.entity.produto import Produto
from application.model.dao.produtoDAO import ProdutoDAO

@app.route("/", methods=['GET'])
def home():
    produto_dao = ProdutoDAO()
    produto_list = produto_dao.listar_todos()
    carrinho_list = produto_dao.mostrar_carrinho()
    return render_template("home.html", carrinho_list=carrinho_list, produto_list=produto_list)