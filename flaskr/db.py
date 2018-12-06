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
        g.cur = conn.cursor()

    return g.cur


def close_db(e=None):
    cur = g.pop('cur', None)
    if cur is not None:
        print("Closing cursor")
        cur.close()
    conn = g.pop('conn', None)
    if conn is not None:
        print("Closing connection")
        conn.close()
