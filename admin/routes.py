from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Product, Category, Enquiry, Dealer
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.check_password(request.form.get('password')):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid username or password', 'danger')
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))
    
    total_products = Product.query.count()
    total_enquiries = Enquiry.query.count()
    new_enquiries = Enquiry.query.filter_by(status='new').count()
    most_viewed = Product.query.order_by(Product.views.desc()).limit(5).all()
    
    # Simple data for charts
    enquiry_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    enquiry_data = [12, 19, 3, 5, 2, 3] # Placeholder data
    
    return render_template('admin/dashboard.html', 
                           total_products=total_products,
                           total_enquiries=total_enquiries,
                           new_enquiries=new_enquiries,
                           most_viewed=most_viewed,
                           enquiry_labels=enquiry_labels,
                           enquiry_data=enquiry_data)

@admin_bp.route('/products', methods=['GET', 'POST'])
@login_required
def manage_products():
    if request.method == 'POST':
        # Add new product
        file = request.files.get('image')
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            
        new_product = Product(
            name=request.form.get('name'),
            category_id=request.form.get('category_id', type=int),
            description=request.form.get('description'),
            material=request.form.get('material'),
            size_range=request.form.get('size_range'),
            application=request.form.get('application'),
            image_url=filename,
            is_featured=bool(request.form.get('is_featured'))
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.manage_products'))
        
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('admin/products.html', products=products, categories=categories)

@admin_bp.route('/enquiries')
@login_required
def manage_enquiries():
    enquiries = Enquiry.query.order_by(Enquiry.created_at.desc()).all()
    return render_template('admin/enquiries.html', enquiries=enquiries)

@admin_bp.route('/enquiries/export')
@login_required
def export_enquiries():
    enquiries = Enquiry.query.all()
    data = []
    for e in enquiries:
        data.append({
            'ID': e.id,
            'Date': e.created_at,
            'Type': e.type,
            'Name': e.name,
            'Email': e.email,
            'Phone': e.phone,
            'Company': e.company_name,
            'Subject': e.subject,
            'Message': e.message,
            'Status': e.status
        })
    df = pd.DataFrame(data)
    filename = f'enquiries_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    filepath = os.path.join(current_app.static_folder, 'exports', filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_excel(filepath, index=False)
    return redirect(url_for('static', filename=f'exports/{filename}'))
