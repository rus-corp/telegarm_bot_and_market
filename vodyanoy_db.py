from config import db_log
import psycopg2


if __name__ == '__main__':
    while True:
        with psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password']) as conn:
            with conn.cursor() as cur:
                pass

