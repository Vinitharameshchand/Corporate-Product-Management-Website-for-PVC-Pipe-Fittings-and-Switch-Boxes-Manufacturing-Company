# Project Report: PVC Manufacturing Management System

## 1. Project Overview
This project is a comprehensive full-stack web application designed for a PVC Pipe Fittings & Switch Boxes Manufacturing company. It serves as both a corporate window for customers and a management tool for administrators.

## 2. Technical Stack
- **Frontend**: HTML5, CSS3 (Custom + Bootstrap 5), JavaScript
- **Backend**: Python 3.x with Flask Framework
- **Database**: MySQL (using SQLAlchemy ORM)
- **Security**: Flask-Login, Werkzeug (Hashing), CSRF Protection (Flask-WTF)
- **Documentation**: Mermaid Diagrams, Markdown

## 3. Key Modules
### A. Product Catalog
- Category-wise listing of PVC fittings and electrical switch boxes.
- Search and filtering functionality.
- Detailed technical specifications for each product.

### B. Enquiries & Leads
- Multiple enquiry types: Individual, Dealer, and RFQ.
- Automated tracking of enquiries in the admin dashboard.
- Direct contact options via WhatsApp and Email.

### C. Admin Dashboard
- Real-time analytics on trending products (most viewed).
- Inventory management (CRUD operations on products).
- Enquiry management with status tracking (New, Follow-up, Closed).
- Data export functionality to Microsoft Excel for offline record-keeping.

### D. Dealer Ecosystem
- Dealer registration system with business verification fields.
- Backend support for dealer-specific logins (Feature ready for expansion).

## 4. Security Features
- **Authentication**: Password hashing using Scrypt for secure admin access.
- **SQL Injection Prevention**: Using SQLAlchemy ORM which uses parameterized queries.
- **CSRF Protection**: Integrated Cross-Site Request Forgery protection on all forms.
- **Session Management**: Secure server-side sessions for admin users.

## 5. Industrial Aesthetics
- **Color Palette**: Professional Blue (`#0d6efd`), Success Green (`#198754`), and Deep Corporate Navy (`#0a2351`).
- **Typography**: Modern sans-serif fonts (Inter & Outfit) for high readability.
- **Responsiveness**: Mobile-first design approach using Bootstrap Grid system.

## 6. Viva-Ready Feature Explanations
1. **How is the Enquiry Export handled?**
   - The system queries the `enquiries` table using SQLAlchemy, converts the result set into a Pandas DataFrame, and uses `openpyxl` to generate an `.xlsx` file which is then served as a download to the admin.
2. **How does the Product Search work?**
   - It utilizes SQL `LIKE` queries on the backend (`Product.name.like(f'%{search_query}%')`) combined with category filtering to provide a responsive search experience.
3. **What is the significance of the `views` column in Products?**
   - It acts as a primary metric for "Dashboard Analytics". Every time a public user visits a specific product page, the counter increments, allowing admins to identify high-demand products.

## 7. Future Scope
- Online Payment Gateway integration for direct B2B orders.
- Inventory low-stock alerts.
- GST-compliant invoice generation from enquiries.
- AI-based demand forecasting based on monthly enquiry trends.
