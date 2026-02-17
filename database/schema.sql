-- Create Database
CREATE DATABASE IF NOT EXISTS manufacturing_db;
USE manufacturing_db;

-- Categories Table
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    specifications JSON,
    material VARCHAR(100),
    size_range VARCHAR(100),
    application VARCHAR(255),
    image_url VARCHAR(255),
    datasheet_url VARCHAR(255),
    is_featured BOOLEAN DEFAULT FALSE,
    views INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Admin Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'staff') DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Enquiries Table
CREATE TABLE IF NOT EXISTS enquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('individual', 'dealer', 'rfq') DEFAULT 'individual',
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    company_name VARCHAR(150),
    subject VARCHAR(200),
    message TEXT NOT NULL,
    product_id INT,
    status ENUM('new', 'in_progress', 'closed') DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL
);

-- Dealers Table
CREATE TABLE IF NOT EXISTS dealers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    company_name VARCHAR(150) NOT NULL,
    gst_number VARCHAR(15),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert Sample Data
INSERT INTO categories (name, description) VALUES 
('PVC Pipe Fittings', 'Durable and high-quality PVC pipe fittings for plumbing and industrial use.'),
('Switch Boxes', 'High-grade electrical switch boxes for residential and commercial applications.');

-- Insert Default Admin (Password: admin123)
-- Hash generated using Werkzeug: pbkdf2:sha256:600000$c6y...
INSERT INTO users (username, email, password_hash, role) VALUES 
('admin', 'admin@manufacturing.com', 'scrypt:32768:8:1$uYk9x3M9G2Lp0Q4Z$c716183e230302484551737be70471900115e24b4249a0f44e13568c09641753966580f865f3a093a152648792013893608cc063e7c8f85f38563309a4d8c89c', 'admin');
