from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(50))
    Phone = Column(String(20))

    # Relationship to orders
    orders = relationship('Order', back_populates='customer', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Customer(ID: {self.ID}, Name: {self.FirstName} {self.LastName}, Email: {self.Email}, Phone: {self.Phone})"


class Product(Base):
    __tablename__ = 'Product'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    Price = Column(Integer)
    StockQuantity = Column(Integer)

    # Relationship to ordered products
    ordered_products = relationship('OrderedProduct', back_populates='product')

    def __repr__(self):
        return f"Product(ID: {self.ID}, Name: {self.Name}, Price: {self.Price}, Stock: {self.StockQuantity})"


class Order(Base):
    __tablename__ = 'Orders'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    OrderDate = Column(Date)
    CustomerID = Column(Integer, ForeignKey('Customer.ID'))

    # Relationship to customer
    customer = relationship('Customer', back_populates='orders')
    # Relationship to ordered products
    ordered_products = relationship('OrderedProduct', back_populates='order', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Order(ID: {self.ID}, Date: {self.OrderDate}, Customer ID: {self.CustomerID})"


class OrderedProduct(Base):
    __tablename__ = 'OrderedProduct'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    OrderID = Column(Integer, ForeignKey('Orders.ID'))
    ProductID = Column(Integer, ForeignKey('Product.ID'))

    # Relationships
    order = relationship('Order', back_populates='ordered_products')
    product = relationship('Product', back_populates='ordered_products')

    def __repr__(self):
        return f"OrderedProduct(ID: {self.ID}, Order ID: {self.OrderID}, Product ID: {self.ProductID})"


