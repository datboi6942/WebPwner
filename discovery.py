# discovery.py

import requests
from bs4 import BeautifulSoup
import config
import utils

def discover_endpoints(base_url):
    """
    Discover all endpoints in the provided base URL by extracting href attributes
    from anchor tags (<a>).
    
    Args:
        base_url (str): The base URL to explore.
    
    Returns:
        List[str]: A list of discovered endpoints.
    """
    try:
        response = requests.get(base_url, headers=config.HEADERS, timeout=config.TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        endpoints = []

        for link in links:
            href = link.get('href')
            if href and href.startswith('/'):
                full_url = base_url.rstrip('/') + href
                endpoints.append(full_url)
            elif href and href.startswith(base_url):
                endpoints.append(href)

        utils.log_info(f"Discovered {len(endpoints)} endpoints.")
        return endpoints
    except requests.RequestException as e:
        utils.log_error(f"Error discovering endpoints: {str(e)}")
        return []