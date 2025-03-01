from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import or_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ------------ Models ------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# ------------ Authentication ------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------ Routes ------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password']
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed! Email/Username already exists', 'danger')
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@app.route('/post_product', methods=['GET', 'POST'])
@login_required
def post_product():
    # Removed user_type check
    if request.method == 'POST':
        try:
            product = Product(
                name=request.form['name'],
                category=request.form['category'],
                price=float(request.form['price']),
                seller_id=current_user.id
            )
            db.session.add(product)
            db.session.commit()
            flash('Product posted successfully!', 'success')
            return redirect(url_for('dashboard'))
        except ValueError:
            flash('Invalid price format!', 'danger')
        except Exception as e:
            db.session.rollback()
            flash('Error posting product!', 'danger')
    
    return render_template('post_product.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    category = request.args.get('category', '')
    
    # Build search conditions
    conditions = []
    if query:
        conditions.append(Product.name.ilike(f'%{query}%'))
    if category:
        conditions.append(Product.category == category)
    
    # Execute query
    if conditions:
        products = Product.query.filter(or_(*conditions)).all()
    else:
        products = Product.query.all()
    
    return render_template('search.html', 
        products=products, 
        query=query, 
        category=category
    )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
