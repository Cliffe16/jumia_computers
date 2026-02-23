from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Let SQLAlchemy securely build the URL and handle all special characters natively
db_url = URL.create(
    drivername="postgresql",
    username="cliffe",  # This strictly forces 'cliffe', ignoring your OS user
    password="BLOOMberg411",  # Put your password with special characters directly here
    host="192.168.100.105",
    port=5432,
    database="jumia_computers"
)

# Create the engine using the safely constructed URL object
engine = create_engine(db_url)

# Export the data
pd.to_sql('raw_data', con=engine, if_exists='replace', index=False)
print("Data successfully exported to Postgres!")
