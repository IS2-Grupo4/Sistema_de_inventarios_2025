from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base de datos (SQLite en un archivo local llamado app.db)
DATABASE_URL = "sqlite:///Backend/app/db/app.db"

# Conexión al motor de SQLAlchemy
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# inspector = inspect(engine)
# print(inspector.get_table_names())

# Sesiones para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base que van a heredar los modelos ORM
Base = declarative_base()


# Dependencia para usar en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()