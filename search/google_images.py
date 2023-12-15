from googleapiclient.discovery import build

def get_image_urls(engine_id, api_key, keywords, exclusions=[], max_images=50):
    """Gets a list of image URLs via the Google custom search API"""
    image_urls = []
    exclude_terms = " ".join(exclusions)

    with build("customsearch", "v1", developerKey=api_key) as service:
        
        url_count = 0
        page_index = 1
        img_count = 10
        cse = service.cse()

        while url_count < max_images:
            
            count_diff = max_images - url_count
            
            if count_diff < 10:
                img_count = count_diff

            response = cse.list(q=keywords, excludeTerms=exclude_terms, cx=engine_id, searchType="image", start=page_index, num=img_count).execute()
            items = response["items"]
            image_urls = image_urls + _parse_items(items)
            
            url_count += len(items)
            page_index += 10
    
    return image_urls

def get_image_urls(engine_id, api_key, keywords, exclusions=[], prefix=None, max_images=50):
    """Gets a list of image URLs via the Google custom search API"""
    image_urls = []
    keyword_str = f'{prefix} {keywords}' if prefix != None else keywords
    exclude_str = " ".join(exclusions)

    with build("customsearch", "v1", developerKey=api_key) as service:
        
        url_count = 0
        page_index = 1
        img_count = 10
        cse = service.cse()

        while url_count < max_images:
            
            count_diff = max_images - url_count
            
            if count_diff < 10:
                img_count = count_diff

            response = cse.list(q=keyword_str, excludeTerms=exclude_str, cx=engine_id, searchType="image", start=page_index, num=img_count).execute()
            items = response["items"]
            image_urls = image_urls + _parse_items(items)
            
            url_count += len(items)
            page_index += 10
    
    return image_urls

def _parse_items(items):
    return [item["link"] for item in items]