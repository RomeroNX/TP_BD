from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Зміни ці параметри відповідно до ваших налаштувань
DATABASE_URL = 'mysql+pymysql://avnadmin:AVNS_Z11J0SsDIVkjyiOkHQI@mysql-f66d937-stud-5f46.d.aivencloud.com:22976/defaultdb'

# Створення двигуна бази даних
engine = create_engine(DATABASE_URL)

# Конфігурація класу Session
Session = sessionmaker(bind=engine)

# Відображення метаданих таблиць, якщо вони вже існують
Base = declarative_base()

def create_session():
    # Створення сесії
    session = Session()
    return session
