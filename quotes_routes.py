# File with the routes of our app

from flask import Blueprint, request, jsonify, current_app
from ConfLoader import ConfLoader
from QuoteCalculator import QuoteCalculator
from config import *

bp = Blueprint('quotes', __name__)

# Error handling
class CustomDataError(Exception):
    '''
    Class for a custom exception when provided data is not correct
    '''
    name = "Custom Data Error"
    code = 400
    description = "Provided data is wrong"

@bp.errorhandler(CustomDataError)
def data_error(error):
    '''
    Simple function to handle all CustomDataError errors.
    '''
    current_app.logger.error(f"Error {error.code}: {error.name} - {error.description}")
    return jsonify({"error": error.name, "description": error.description}), error.code

# Routes
@bp.route('/build_quote', methods=['POST'])
def build_quote():
    '''
    POST: Calculate the final quotes from provider based on the requested topics
    '''
    # Get data from the request
    data = request.get_json()

    # Check if data is correct
    if not data or "topics" not in data:
        raise CustomDataError()

    # Prepare provider data
    confLoader = ConfLoader(conf_file_name)
    provider_topics = confLoader.prepare_provider_conf()

    # Get the final quotes
    quoteCalculator = QuoteCalculator(data, provider_topics)
    final_quotes = quoteCalculator.get_final_quotes()

    current_app.logger.info("Quote build successful!")

    # Return the quote as JSON
    return jsonify(final_quotes), 200