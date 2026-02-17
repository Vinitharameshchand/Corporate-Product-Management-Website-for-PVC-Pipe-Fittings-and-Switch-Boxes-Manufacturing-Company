from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
from models import db, Product, Category, Enquiry, Dealer, User
from flask_login import login_user, logout_user, login_required, current_user
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True).limit(6).all()
    categories = Category.query.all()
    return render_template('index.html', featured_products=featured_products, categories=categories)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/products')
def products():
    category_id = request.args.get('category', type=int)
    search_query = request.args.get('search', '')
    
    query = Product.query
    if category_id:
        query = query.filter_by(category_id=category_id)
    if search_query:
        query = query.filter(Product.name.like(f'%{search_query}%'))
    
    products_list = query.all()
    categories = Category.query.all()
    return render_template('products.html', products=products_list, categories=categories, selected_category=category_id)

@main_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    product.views += 1
    db.session.commit()
    return render_template('product_detail.html', product=product)

@main_bp.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    if request.method == 'POST':
        new_enquiry = Enquiry(
            type=request.form.get('type', 'individual'),
            name=request.form.get('name'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            company_name=request.form.get('company_name'),
            subject=request.form.get('subject'),
            message=request.form.get('message'),
            product_id=request.form.get('product_id', type=int)
        )
        db.session.add(new_enquiry)
        db.session.commit()
        flash('Your enquiry has been submitted successfully! We will contact you soon.', 'success')
        return redirect(url_for('main.enquiry'))
    
    product_id = request.args.get('product_id', type=int)
    product = None
    if product_id:
        product = Product.query.get(product_id)
        
    return render_template('enquiry.html', product=product)

@main_bp.route('/dealer/register', methods=['GET', 'POST'])
def dealer_register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('main.dealer_register'))
            
        new_user = User(username=username, email=email, role='dealer')
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.flush() # Get ID before commit
        
        new_dealer = Dealer(
            user_id=new_user.id,
            company_name=request.form.get('company_name'),
            gst_number=request.form.get('gst_number'),
            address=request.form.get('address'),
            city=request.form.get('city'),
            state=request.form.get('state')
        )
        db.session.add(new_dealer)
        db.session.commit()
        
        flash('Registration successful! Please login after approval.', 'success')
        return redirect(url_for('admin.login'))
        
    return render_template('dealer_register.html')
