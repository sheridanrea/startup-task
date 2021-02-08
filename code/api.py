# API for houses data
import psycopg2 as pgp2
from possibilities import *

# Opens db connection and sets cursor
def open_conn():
    # set up connection
    conn = pgp2.connect(
        database="postgres",
        user="postgres",
        password="supersecret",
        host="localhost",
        port="5432"
    )
    return conn, conn.cursor()


# Closes db connection
def close_conn(cur, conn):
    cur.close()
    conn.close()


# Warm up function
# Lets user get all data on houses of a particular color(s)
def get_color_house(colors):
    (conn, cur) = open_conn()
    if type(colors) == str:
        colors = [colors]
    paramspec = ",".join(["%s"] * len(colors))
    color_command = (
        "SELECT * \
        FROM houses \
        WHERE color IN ({}) \
        "
    )
    cur.execute(color_command.format(paramspec), colors)
    results = cur.fetchall()
    close_conn(cur, conn)
    return results


# Returns subset of data specified by user, default returns whole dataset
# Would want more sanity checks on user input
def gen_data(colors=COLORS, price_less_than=MAX_PRICE, sqft_at_least=0, constructed_after=0):
    (conn, cur) = open_conn()
    if type(colors) == str:
        colors = [colors]
    paramspec = ",".join(["%s"] * len(colors))
    color_command = (
        "SELECT * \
        FROM houses \
        WHERE color IN ({}) \
        AND price <= %s \
        AND sq_ft >= %s \
        AND date_constructed > %s \
        "
    )
    # don't like this, but don't want to import more libraries right now
    params = list(colors)
    other_params = [price_less_than, sqft_at_least, constructed_after]
    for item in other_params:
        params.append(item)
    cur.execute(color_command.format(paramspec), params)
    results = cur.fetchall()
    close_conn(cur, conn)
    return results