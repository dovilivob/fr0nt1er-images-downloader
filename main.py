import json
import time
from os.path import exists
from bing_image_downloader import downloader


search_words = ['city', 'forest', 'lake']

if __name__ == '__main__':
    for word in search_words:
        folder_name_suffix = 0
        while exists(f'{word}/{folder_name_suffix}'):
            folder_name_suffix += 1

        downloader.download(
            word,
            limit=10000,
            output_dir=f'images/{word}/{folder_name_suffix}',
            adult_filter_off=True,
            force_replace=False,
            timeout=60,
            verbose=True
        )

    time.sleep(2)
