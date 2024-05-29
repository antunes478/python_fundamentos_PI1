from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados fictícios de produtos
produtos = [
    {"id": 1, "nome": "Processador Intel Core i9 12900K", "descricao": "Processador Intel Core i9-12900K, 16 Cores, Socket LGA1700", "preco": 215, "imagem": "processador.jpeg"},
    # Adicione mais produtos aqui
]

# Inicialização da lista de produtos no carrinho de compras
produtos_no_carrinho = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Processar o formulário de adição de produto
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        imagem = request.form['imagem']
        
        # Gerar um novo id para o produto
        novo_id = max(produtos, key=lambda x: x['id'])['id'] + 1 if produtos else 1
        novo_produto = {"id": novo_id, "nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
        
        # Adicionar o novo produto à lista de produtos
        produtos.append(novo_produto)
        
        # Redirecionar para a página inicial
        return redirect(url_for('index'))
    
    # Se o método for GET, exibir o formulário de adição de produto
    return render_template('add_product.html')

@app.route('/carrinho_de_compras')
def carrinho_de_compras():
    total = sum(produto['preco'] for produto in produtos_no_carrinho)
    return render_template('carrinho_de_compras.html', produtos=produtos_no_carrinho, total=total)

if __name__ == '__main__':
    app.run(debug=True)
