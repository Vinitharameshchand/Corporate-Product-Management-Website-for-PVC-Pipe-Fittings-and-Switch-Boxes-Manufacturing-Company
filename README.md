# Professional PVC Manufacturing Management System

A production-ready full-stack web application for PVC Pipe Fittings and Switch Boxes manufacturing businesses.

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- MySQL Server (XAMPP/WAMP recommended)

### 2. Setup
```bash
# Clone the repository
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Configuration
1. Create a MySQL database named `manufacturing_db`.
2. Update the connection string in `config.py` if necessary.
3. Run the initialization script to create tables and sample data:
```bash
python database/init_db.py
```

### 4. Run the Application
```bash
python app.py
```
Access the website at `http://127.0.0.1:5000`

## 🔐 Admin Access
- **URL**: `http://127.0.0.1:5000/admin/login`
- **Username**: `admin`
- **Password**: `admin123`

## 📁 Project Structure
- `/admin`: Admin blueprints and logic.
- `/database`: SQL schema and initialization scripts.
- `/models`: SQLAlchemy database models.
- `/routes`: Frontend route handlers.
- `/static`: CSS, Javascript, and product images.
- `/templates`: HTML templates using Jinja2.
- `/documentation`: Project report and ER diagrams.

## ✨ Key Features
- **Responsive Design**: Optimized for desktop, tablet, and mobile.
- **Product Management**: Complete CRUD for manufacturing products.
- **Dashboard Analytics**: Visual charts for enquiry trends and product views.
- **Dealer Network**: Registration system for business partners.
- **Lead Generation**: Multi-type enquiry forms (Individual, Dealer, RFQ).
- **Excel Export**: Bulk export of enquiries for business analysis.
