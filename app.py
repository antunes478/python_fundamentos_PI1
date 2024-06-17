import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask import Flask

# Define o caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# Configura a aplicação Flask
app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'), static_folder=os.path.join(basedir, 'static'))

# Imprime o caminho da pasta de templates e estática
print("Pasta de templates:", app.template_folder)
print("Pasta de estáticos:", app.static_folder)


app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'mydb.db')

# Verificar se o diretório 'instance' existe, senão, criar
instance_path = os.path.join(basedir, 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if not username or not email or not password:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Nome de usuário já em uso. Por favor, escolha outro.', 'error')
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('E-mail já em uso. Por favor, use outro e-mail.', 'error')
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registro realizado com sucesso. Faça login para continuar.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = "Nome de usuário ou senha inválidos. Tente novamente."
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route('/notebooks')
@login_required
def notebooks():
    notebooks = Product.query.filter_by(category='notebooks').all()
    return render_template('notebooks.html', products=notebooks)

@app.route('/pcs')
@login_required
def pcs():
    pcs = Product.query.filter_by(category='pcs').all()
    return render_template('pcs.html', products=pcs)

@app.route('/mouse')
@login_required
def mouse():
    mouses = Product.query.filter_by(category='mouse').all()
    return render_template('mouse.html', products=mouse)

@app.route('/fones')
@login_required
def fones():
    fones = Product.query.filter_by(category='fones').all()
    return render_template('fones.html', products=fones)


@app.route('/cadeiras_gamer')
def cadeiras_gamer():
    return render_template('cadeiras_gamer.html')

@app.route('/teclados')
def teclados():
    return render_template('teclados.html')

@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        # Lógica para adicionar um novo produto
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')
        new_product = Product(name=name, price=price, category=category)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial após adicionar o produto
    return render_template('add_product.html')

@app.route('/delete_product/<int:id>')
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')

@app.route('/add_to_cart/<int:id>')
@login_required
def add_to_cart(id):
    # Adicionar lógica para adicionar ao carrinho
    return redirect(url_for('index'))

@app.route('/checkout')
@login_required
def checkout():
    # Processar a compra (exemplo simplificado)
    if 'cart' in session and len(session['cart']) > 0:
        # Salvar os itens do carrinho no banco de dados ou processar o pagamento
        session.pop('cart')  # Limpar o carrinho após a compra

        flash('Compra realizada com sucesso!', 'success')
        return redirect(url_for('index'))
    
    flash('Seu carrinho está vazio.', 'info')
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
