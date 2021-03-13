from flask import Flask


def init_app(app: Flask):
    @app.route("/")
    def index():
        return "<h1>Hola Flask</h1>"

    @app.route("/about/<string:nome>/")
    def about(nome):
        return f'My name is {nome}'

    @app.route("/blog")
    def blog():
        return "<form>login in</form>"
