from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from extensions import db, login_manager
from models import User, Product
import os
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secure_key_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
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
                username=request.form.get('username'),
                email=request.form.get('email'),
                password=request.form.get('password')
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login', 'success')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('Email/Username already exists!', 'danger')
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@app.route('/post_product', methods=['GET', 'POST'])
@login_required
def post_product():
    if request.method == 'POST':
        try:
            # File handling
            file = request.files['image']
            if file.filename == '' or not allowed_file(file.filename):
                flash('Invalid image file!', 'danger')
                return redirect(request.url)
            
            filename = secure_filename(f"{int(time.time())}_{file.filename}")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Create product
            product = Product(
                name=request.form.get('name'),
                category=request.form.get('category'),
                price=float(request.form.get('price')),
                image=filename,
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
    
    conditions = []
    if query: 
        conditions.append(Product.name.ilike(f'%{query}%'))
    if category: 
        conditions.append(Product.category == category)
    
    products = Product.query.filter(*conditions).all() if conditions else Product.query.all()
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
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
