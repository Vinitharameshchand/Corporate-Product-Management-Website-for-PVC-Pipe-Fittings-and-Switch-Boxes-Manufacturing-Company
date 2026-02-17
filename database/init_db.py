from app import app
from models import db, Category, Product, User, Enquiry
from werkzeug.security import generate_password_hash
import json

def init():
    with app.app_context():
        # Drop and create tables
        db.drop_all()
        db.create_all()

        # Add Categories
        cat1 = Category(name='PVC Pipe Fittings', description='Durable and high-quality PVC pipe fittings for plumbing and industrial use.')
        cat2 = Category(name='Switch Boxes', description='High-grade electrical switch boxes for residential and commercial applications.')
        db.session.add(cat1)
        db.session.add(cat2)
        db.session.flush()

        # Add Default Admin (admin/admin123)
        admin = User(username='admin', email='admin@vinithapvc.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        # Add Sample Products
        p1 = Product(
            name='UPVC Elbow 90 Degree',
            category_id=cat1.id,
            description='Heavy duty 90 degree elbow for plumbing systems. High pressure resistant.',
            material='UPVC',
            size_range='20mm - 110mm',
            application='Residential Plumbing',
            is_featured=True,
            specifications={
                "Tensile Strength": "45 MPa",
                "Color": "White",
                "Standard": "IS 4985"
            }
        )
        
        p2 = Product(
            name='Concealed Switch Box 4-Way',
            category_id=cat2.id,
            description='Premium quality concealed switch box with 4 module capacity. Flame retardant.',
            material='Polycarbonate',
            size_range='4 Module',
            application='House Wiring',
            is_featured=True,
            specifications={
                "Fire Resistance": "V0 Grade",
                "Modules": "4",
                "Finish": "Glossy White"
            }
        )

        p3 = Product(
            name='PVC Coupler',
            category_id=cat1.id,
            description='Standard PVC coupler for leak-proof pipe joining.',
            material='PVC',
            size_range='1/2" - 4"',
            application='Industrial Fluids',
            is_featured=True
        )

        db.session.add_all([p1, p2, p3])
        
        # Add Sample Enquiry
        e1 = Enquiry(
            name='Vikas Kumar',
            email='vikas@example.com',
            phone='+91 9988776655',
            subject='Bulk order for construction project',
            message='I need 500 units of UPVC elbows and 200 switch boxes for an upcoming residential project in Pune.',
            type='dealer'
        )
        db.session.add(e1)

        db.session.commit()
        print("Database initialized with sample data successfully!")

if __name__ == '__main__':
    init()
