from time import sleep
from search.queries import to_query_str
import requests

def get_image_urls(subscription_key, keywords, exclusions=[], prefix=None, max_images=50):
    """Returns a list of URLs for images via the Bing Image Search API"""
    search_url = "https://api.bing.microsoft.com/v7.0/images/search"

    query_str = to_query_str(keywords, exclusions, prefix)

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": query_str, "count": max_images}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    sleep(1)
    return [img["contentUrl"] for img in search_results["value"]]