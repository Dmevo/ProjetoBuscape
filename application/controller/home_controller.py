from flask import render_template, url_for, request, jsonify
from application import app
from application.model.entity.produto import Produto
from application.model.dao.produtoDAO import ProdutoDAO

produto_dao = ProdutoDAO()
produto_list = produto_dao.listar_todos()
carrinho_list = produto_dao.mostrar_carrinho()

@app.route("/")
def home():
    return render_template("home.html", carrinho_list=carrinho_list, produto_list=produto_list)

@app.route("/add/<id>")
def add(id):
    for produto in produto_list:
        if  produto.get_id() == int(id):
            carrinho_list.append(produto) 
    return render_template("home.html", carrinho_list=carrinho_list, produto_list=produto_list)

@app.route("/delete/<id>")
def delete(id):
    for produto in carrinho_list:
        if produto.get_id() == int(id):
            carrinho_list.remove(produto)
    return render_template("home.html", carrinho_list=carrinho_list, produto_list=produto_list)


