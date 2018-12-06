import os

from flask import Flask
from flask import current_app, g

# TODO:
# get_db function with tear_down function and base boilerplate
# create own project with git repo
# formulate task(s)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        try:
            app.config.from_pyfile('config.cfg', silent=False)
        except FileNotFoundError:
            print("You need to provide a config.cfg file in the instance folder.")
            app.config.from_mapping(
                DATABASE_NAME='your_db',
                USER='your_user',
                PWD='your_pwd',
                SECRET_KEY='your_key'
            )
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # PLEASE NOTE:
    # Flask has a great templating feature that is not used here by intend, in order to:
    # - simplify things
    # - to show what is going on based on a low level

    # render a list here
    @app.route('/start', methods=('GET', 'POST'))
    def start():
        print(current_app.config['DATABASE_NAME'], )

        html = '<html><head><title="wow"></head>' \
               '<body>' \
               '<h1>a list of db entries</h1>' \
               '<ul>' \
               '<li><a href="/1/detail">follow link</a></li>' \
               '</ul>' \
               '</body></html>'
        return html

    # show a detail here
    @app.route('/<int:db_id>/detail', methods=('GET', 'POST'))
    def detail(db_id):
        html = '<html><head><title="wow"></head>' \
               '<body>' \
               '<h1>a informative detail page on a specific id</h1>' \
               'id == {}' \
               '</body></html>'.format(db_id)
        return html

    return app
