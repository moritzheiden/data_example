import urllib
import gzip
import os
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path, which_data):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=f'/{output_path}{which_data}', reporthook=t.update_to)

def download_file(url, output_path, which_data):
    # Download archive
    try:
        # check if file already exists

        if os.path.isfile(f'{output_path}{which_data}'):
            pass
        else:
            download_url(url, output_path, which_data)

        with gzip.open(f'{output_path}{which_data}', 'rb') as s_file, \
                open(f'{output_path}{which_data.strip(".gz")}', 'wb') as d_file:
            while True:
                block = s_file.read(65536)
                if not block:
                    break
                else:
                    d_file.write(block)

    except Exception as e:
        print(e)
        return 1