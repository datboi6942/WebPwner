# request_handler.py

import requests
import config
import utils
import logger

def send_get_request(url, params=None, headers=None):
    """
    Send a GET request to the specified URL with optional parameters and headers.

    Args:
        url (str): The URL to send the GET request to.
        params (dict): Optional dictionary of query parameters.
        headers (dict): Optional dictionary of HTTP headers.

    Returns:
        requests.Response: The response object from the request, or None if failed.
    """
    if headers is None:
        headers = config.HEADERS
    
    logger.log_request(url, 'GET', params)
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=config.TIMEOUT)
        response.raise_for_status()
        utils.log_info(f"GET request to {url} successful.")
        return response
    except requests.RequestException as e:
        utils.log_error(f"GET request to {url} failed: {str(e)}")
        return None

def send_post_request(url, data=None, json=None, headers=None):
    """
    Send a POST request to the specified URL with optional data, JSON, and headers.

    Args:
        url (str): The URL to send the POST request to.
        data (dict): Optional dictionary of form data.
        json (dict): Optional JSON payload.
        headers (dict): Optional dictionary of HTTP headers.

    Returns:
        requests.Response: The response object from the request, or None if failed.
    """
    if headers is None:
        headers = config.HEADERS
    
    logger.log_request(url, 'POST', data or json)
    
    try:
        response = requests.post(url, data=data, json=json, headers=headers, timeout=config.TIMEOUT)
        response.raise_for_status()
        utils.log_info(f"POST request to {url} successful.")
        return response
    except requests.RequestException as e:
        utils.log_error(f"POST request to {url} failed: {str(e)}")
        return None

def send_payload(url, payload, method='GET', headers=None):
    """
    Send a crafted payload to the specified URL using the specified method.

    Args:
        url (str): The URL to send the payload to.
        payload (dict): The payload data to send (as params for GET, data for POST).
        method (str): The HTTP method to use ('GET' or 'POST').
        headers (dict): Optional dictionary of HTTP headers.

    Returns:
        requests.Response: The response object from the request, or None if failed.
    """
    if headers is None:
        headers = config.HEADERS
    
    logger.log_request(url, method, payload)
    
    if method.upper() == 'GET':
        return send_get_request(url, params=payload, headers=headers)
    elif method.upper() == 'POST':
        return send_post_request(url, data=payload, headers=headers)
    else:
        utils.log_error(f"Unsupported HTTP method: {method}")
        return None