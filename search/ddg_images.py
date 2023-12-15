from fastbook import search_images_ddg
from common_image_tools.queries import to_query_str

#For naming consistency, this just wraps the fastai function:
def get_image_urls(keywords, exclusions=[], prefix=None, max_images=50):
  """Returns a list of image URLs via DuckDuckGo"""
  query = to_query_str(keywords, exclusions, prefix)
  return search_images_ddg(query, max_images=max_images)