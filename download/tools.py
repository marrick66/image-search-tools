import shutil
from fastbook import download_images as fastai_download

def download_images(path, image_urls):
    """Downloads images from the URLs specified and saves them to the path given."""

    if path.exists():
        shutil.rmtree(path)

    path.mkdir()

    fastai_download(path, urls=image_urls)

def download_imageset(image_dict, root_path):
    """For the dictionary of search terms and image URLs, downloads them into subdirectories underneath the root path.
    """
    if root_path.exists():
        shutil.rmtree(root_path)

    root_path.mkdir()
    
    for key in image_dict:
      path = (root_path/key)
      download_images(path, image_dict[key])