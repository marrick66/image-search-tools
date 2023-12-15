import shutil
from fastbook import download_images as fastai_download

def download_images(path, image_urls):

    if path.exists():
        shutil.rmtree(path)

    path.mkdir()

    fastai_download(path, urls=image_urls)