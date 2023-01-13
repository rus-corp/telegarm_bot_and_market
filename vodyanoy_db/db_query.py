import asyncio
import psycopg2
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from config import db_log




def get_gas_heater(price):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT maker, name, price FROM product
        WHERE price > %s AND categories_id = 2""", [price]
        )
        conn.commit()
        load = cur.fetchall()        
        for i in load:
            return i

    conn.close()


# asyncio.run(get_gas_heater(price))
