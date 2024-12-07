from database import create_session
from models import Customer, Product, Order

def show_menu():
    print("1. Показати всі таблиці")
    print("2. Показати Customers")
    print("3. Показати Products")
    print("4. Показати Orders")
    print("5. Додати новий Product")
    print("6. Видалити Order з ID 1")
    print("7. Видалити Customer разом із його Orders")
    print("8. Змінити дату Order з ID 3")
    print("9. Вихід")

def print_table_data(query):
    for row in query:
        print(row)

def add_product(session):
    name = input("Введіть назву продукту: ")
    price = int(input("Введіть ціну продукту: "))
    stock_quantity = int(input("Введіть кількість на складі: "))

    new_product = Product(Name=name, Price=price, StockQuantity=stock_quantity)
    session.add(new_product)
    session.commit()
    print("Продукт додано успішно.")

def delete_order_by_id(session, order_id):
    order_to_delete = session.query(Order).filter(Order.ID == order_id).first()
    if order_to_delete:
        session.delete(order_to_delete)
        session.commit()
        print(f"Order з ID {order_id} видалено успішно.")
    else:
        print(f"Order з ID {order_id} не знайдено.")

def delete_customer_with_orders(session, customer_id):
    customer_to_delete = session.query(Customer).filter(Customer.ID == customer_id).first()
    if customer_to_delete:
        session.delete(customer_to_delete)
        session.commit()
        print(f"Customer з ID {customer_id} та всі його Orders видалено успішно.")
    else:
        print(f"Customer з ID {customer_id} не знайдено.")

def update_order_date(session, order_id):
    order_to_update = session.query(Order).filter(Order.ID == order_id).first()
    if order_to_update:
        new_date = input("Введіть нову дату замовлення (у форматі YYYY-MM-DD): ")
        try:
            from datetime import datetime
            order_to_update.OrderDate = datetime.strptime(new_date, "%Y-%m-%d").date()
            session.commit()
            print(f"Дата замовлення з ID {order_id} змінена на {new_date}.")
        except ValueError:
            print("Невірний формат дати. Спробуйте ще раз.")
    else:
        print(f"Замовлення з ID {order_id} не знайдено.")

def main():
    session = create_session()

    if session:
        while True:
            show_menu()
            choice = input("Введіть команду: ")

            if choice == "1":
                print("Customers:")
                print_table_data(session.query(Customer).all())
                print("\nProducts:")
                print_table_data(session.query(Product).all())
                print("\nOrders:")
                print_table_data(session.query(Order).all())

            elif choice == "2":
                print_table_data(session.query(Customer).all())
            elif choice == "3":
                print_table_data(session.query(Product).all())
            elif choice == "4":
                print_table_data(session.query(Order).all())
            elif choice == "5":
                add_product(session)
            elif choice == "6":
                delete_order_by_id(session, order_id=1)
            elif choice == "7":
                customer_id = int(input("Введіть ID Customer для видалення: "))
                delete_customer_with_orders(session, customer_id)
            elif choice == "8":
                update_order_date(session, order_id=3)
            elif choice == "9":
                break
            else:
                print("Невідома команда")
    else:
        print("Не вдалося встановити з'єднання.")

if __name__ == "__main__":
    main()
