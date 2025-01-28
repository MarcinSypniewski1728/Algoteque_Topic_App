# File with the routes of our app

from flask import Blueprint, request, jsonify
from ConfLoader import ConfLoader
from QuoteCalculator import QuoteCalculator
from config import *

bp = Blueprint('quotes', __name__)

@bp.route('/build_quote', methods=['POST'])
def build_quote():
    '''
    POST: Calculate the final quotes from provider based on the requested topics
    '''
    # Get data from the request

    data = request.get_json()

    # Check if data is correct
    if not data or "topics" not in data:
        return jsonify({"error": "Invalid JSON input"}), 400


    # Prepare provider data
    confLoader = ConfLoader(conf_file_name)
    provider_topics = confLoader.prepare_provider_conf()

    # Get the final quotes
    quoteCalculator = QuoteCalculator(data, provider_topics)
    final_quotes = quoteCalculator.get_final_quotes()

    # Return the quote as JSON
    return jsonify(final_quotes), 200