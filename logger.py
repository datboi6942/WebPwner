import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_request(url, method, payload):
    """
    Log the details of an HTTP request.

    Args:
        url (str): The URL of the request.
        method (str): The HTTP method used.
        payload (dict): The payload sent with the request.
    """
    logging.info(f"Request - URL: {url}, Method: {method}, Payload: {payload}")

def log_response(response):
    """
    Log the details of an HTTP response.

    Args:
        response (requests.Response): The response object.
    """
    logging.info(f"Response - Status Code: {response.status_code}, Body: {response.text}")

def log_ai_response(prompt, ai_response):
    """
    Log the details of an AI response.

    Args:
        prompt (str): The prompt sent to the AI.
        ai_response (str): The response from the AI.
    """
    logging.info(f"AI Prompt: {prompt}")
    logging.info(f"AI Response: {ai_response}")
