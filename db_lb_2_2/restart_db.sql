-- Active: 1733061667435@@mysql-f66d937-stud-5f46.d.aivencloud.com@22976@defaultdb
-- Видалення таблиць, якщо вони існують
DROP TABLE IF EXISTS OrderedProduct;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Customer;

-- Створення таблиці Customer
CREATE TABLE Customer (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(50),
    Phone VARCHAR(20)
);

-- Створення таблиці Product
CREATE TABLE Product (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Price INT,
    StockQuantity INT
);

-- Створення таблиці Orders
CREATE TABLE Orders (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(ID) ON DELETE CASCADE
);

-- Створення таблиці OrderedProduct
CREATE TABLE OrderedProduct (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(ID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Product(ID) ON DELETE CASCADE
);

-- Вставлення записів у таблицю Customer
INSERT INTO Customer (FirstName, LastName, Email, Phone) VALUES
('Alisa', 'Smith', 'alisa.smith@example.com', '1234567890'),
('Vladyslav', 'Johnson', 'vlad.johnson@example.com', '2345678901'),
('Anastasia', 'Brown', 'anastasia.brown@example.com', '3456789012'),
('Daria', 'Taylor', 'daria.taylor@example.com', '4567890123'),
('Щур', 'Davis', 'alisa.davis@example.com', '5678901234');

-- Вставлення записів у таблицю Product
INSERT INTO Product (Name, Price, StockQuantity) VALUES
('Laptop', 1000, 10),
('Smartphone', 800, 20),
('Tablet', 500, 15),
('Headphones', 150, 50),
('Smartwatch', 200, 25);

-- Вставлення записів у таблицю Orders
INSERT INTO Orders (OrderDate, CustomerID) VALUES
('2024-12-01', 1),
('2024-12-02', 2),
('2024-12-03', 3),
('2024-12-04', 4),
('2024-12-05', 5);

-- Вставлення записів у таблицю OrderedProduct
INSERT INTO OrderedProduct (OrderID, ProductID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
