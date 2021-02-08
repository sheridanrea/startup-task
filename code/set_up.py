# Set up database with random data
import psycopg2 as pgp2
import random
from possibilities import *
NUM_ROWS = 10

# all this should have error checking
# connect to db
conn = pgp2.connect(
    database="postgres",
    user="postgres",
    password="supersecret",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create houses table with
# color, price, size, date constructed
def create_table():
    create_table_command = (
        """
        CREATE TABLE houses (
            house_id SERIAL PRIMARY KEY,
            color VARCHAR(255),
            price NUMERIC,
            sq_ft NUMERIC,
            date_constructed INTEGER
        )
        """
    )
    cur.execute(create_table_command)

def add_random_data(n):
    house_data = [[random.choice(COLORS), random.randint(MIN_PRICE, MAX_PRICE), random.randint(MIN_SQFT, MAX_SQFT), random.randint(MIN_DATE, MAX_DATE)] for x in range(n)]
    insert_data_sql = " INSERT INTO houses (color, price, sq_ft, date_constructed) VALUES (%s, %s, %s, %s)"
    cur.executemany(insert_data_sql, house_data)

create_table()
add_random_data(NUM_ROWS)

conn.commit()
cur.close()
conn.close()