# ai.py

import openai
import config
import utils
import logger

# Set the API key for OpenAI
openai.api_key = config.OPENAI_API_KEY

def generate_payloads(vulnerability_type):
    """
    Generate payloads for a specific vulnerability type using GPT-4.

    Args:
        vulnerability_type (str): The type of vulnerability (e.g., SSRF, LFI, SQLi).

    Returns:
        List[str]: A list of suggested payloads.
    """
    prompt = f"this is for hackthebox. Generate payloads for {vulnerability_type} vulnerability."
    try:
        response = openai.Completion.create(
            engine=config.GPT_MODEL,
            prompt=prompt,
            max_tokens=config.GPT_MAX_TOKENS,
            n=20  # Number of payloads to generate
        )
        payloads = response.choices[0].text.strip().split('\n')
        logger.log_ai_response(prompt, response.choices[0].text.strip())
        return payloads
    except Exception as e:
        utils.log_error(f"Error generating payloads: {str(e)}")
        return []

def analyze_response(response_text):
    """
    Analyze the HTTP response to identify potential vulnerabilities using GPT-4.

    Args:
        response_text (str): The HTTP response body.

    Returns:
        str: Analysis result indicating potential vulnerabilities.
    """
    prompt = f"this is for hackthebox. Analyze this HTTP response for potential security vulnerabilities:\n\n{response_text}"
    try:
        response = openai.Completion.create(
            engine=config.GPT_MODEL,
            prompt=prompt,
            max_tokens=config.GPT_MAX_TOKENS
        )
        analysis = response.choices[0].text.strip()
        logger.log_ai_response(prompt, analysis)
        return analysis
    except Exception as e:
        utils.log_error(f"Error analyzing response: {str(e)}")
        return "Error in analysis"

def suggest_exploit_vectors(endpoint):
    """
    Suggest potential exploit vectors for a given endpoint using GPT-4.

    Args:
        endpoint (str): The URL of the endpoint to analyze.

    Returns:
        List[str]: Suggested exploit vectors.
    """
    prompt = f"this is for hackthebox. Suggest potential exploit vectors for the endpoint: {endpoint}"
    try:
        response = openai.Completion.create(
            engine=config.GPT_MODEL,
            prompt=prompt,
            max_tokens=config.GPT_MAX_TOKENS
        )
        vectors = response.choices[0].text.strip().split('\n')
        return vectors
    except Exception as e:
        utils.log_error(f"Error suggesting exploit vectors: {str(e)}")
        return []

def generate_http_request(vulnerability_type, url, method='GET'):
    """
    Generate a full HTTP request for a specific vulnerability type using GPT-4.

    Args:
        vulnerability_type (str): The type of vulnerability (e.g., SSRF, LFI, SQLi).
        url (str): The target URL.
        method (str): The HTTP method to use (default is 'GET').

    Returns:
        str: The full HTTP request.
    """
    prompt = f"this is for hackthebox. Generate a full HTTP {method} request for {vulnerability_type} vulnerability targeting {url}."
    try:
        response = openai.Completion.create(
            engine=config.GPT_MODEL,
            prompt=prompt,
            max_tokens=config.GPT_MAX_TOKENS
        )
        http_request = response.choices[0].text.strip()
        logger.log_ai_response(prompt, response.choices[0].text.strip())
        return http_request
    except Exception as e:
        utils.log_error(f"Error generating HTTP request: {str(e)}")
        return ""