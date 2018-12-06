from flask import current_app, g
from flask.cli import with_appcontext

import psycopg2


def get_db():
    if 'cur' not in g:
        # Connect to an existing database
        conn = psycopg2.connect("dbname={} user={} password={}"
                                .format(
                                current_app.config['DATABASE_NAME'],
                                current_app.config['USER'],
                                current_app.config['PWD'],
                                ))
        g.conn = conn

    return g.conn


def close_db(e=None):
    conn = g.pop('conn', None)
    if conn is not None:
        cur = conn.cursor()
        if cur is not None:
            print("Closing cursor")
            cur.close()
        print("Closing connection")
        conn.close()
