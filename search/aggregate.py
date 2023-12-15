from search import bing_images as bing
from search import google_images as google
from search import ddg_images as ddg

def get_image_urls(keywords, exclusions=[], prefix=None, bing_creds=None, google_creds=None, max_images=50):
    """Returns a list of image URLs aggregated from the combination of DuckDuckGo, Bing, and Google APIs."""
    engine_id, api_key = google_creds if google_creds != None else (None, None)
    subscription_key = bing_creds if bing_creds != None else None

    image_urls = []

    if engine_id != None and api_key != None:
        image_urls = image_urls + google.get_image_urls(engine_id, api_key, keywords, exclusions, prefix, max_images)

    if subscription_key != None:
        image_urls = image_urls + bing.get_image_urls(subscription_key, keywords, exclusions, prefix, max_images)

    image_urls = image_urls + ddg.get_image_urls(keywords, exclusions, prefix, max_images)

    return image_urls

def get_image_dict(keyword_dict, prefix=None, bing_creds=None, google_creds=None, max_images=50):

    image_dict = {}

    for keyword in keyword_dict:
        exclusions = keyword_dict[keyword]
        image_urls = get_image_urls(keyword, exclusions, prefix, bing_creds, google_creds, max_images)
        image_dict[keyword] = image_urls

    return image_dict