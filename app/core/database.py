from databases import Database
from sqlalchemy import MetaData
import os

# Load DATABASE_URL from env
DATABASE_URL = os.getenv("DATABASE_URL")

# The database connection (databases library)
database = Database(DATABASE_URL)

# The SQLAlchemy metadata registry (for tables.py to register tables)
metadata = MetaData()
