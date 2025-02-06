# Main file to run the app

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

from quotes_routes import bp as quotes_bp
app.register_blueprint(quotes_bp)

# Global error handling
@app.errorhandler(HTTPException)
def http_error(error):
    '''
    Simple function to handle all HTTP errors.
    '''
    app.logger.error(f"Error {error.code}: {error.name} - {error.description}")
    return jsonify({"error": error.name, "description": error.description}), error.code

@app.errorhandler(Exception)
def other_error(error):
    '''
    Simple function to handle all other unexpected errors.
    '''
    app.logger.error(f"Error {error.code}: {error.name} - {error.description}")
    return jsonify({"error": error.name, "description": error.description}), error.code

# Initialization
if __name__ == '__main__':
    # Define rotating logger to save disk space
    handler = RotatingFileHandler("record.log", maxBytes=5*1024*1024, backupCount=3)
    # Set logging format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    app.run()
