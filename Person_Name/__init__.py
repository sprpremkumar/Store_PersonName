from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key="ugdifasdfhu"

    from . import Person_Name
    app.register_blueprint(Person_Name.bp)

    return app

