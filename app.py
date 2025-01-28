# Main file to run the app

from flask import Flask

app = Flask(__name__)

from quotes_routes import bp as quotes_bp
app.register_blueprint(quotes_bp)

if __name__ == '__main__':
    app.run(debug=True)
