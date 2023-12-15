import requests
import re
import tarfile
from io import BytesIO
from urllib.parse import urljoin
from tqdm import tqdm
import time
# html_page_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/00/00/'

def download_and_unzip_from_html(html_url):
   # Fetch the HTML content
    response = requests.get(html_url)
    if response.status_code != 200:
        print("Failed to fetch HTML content")
        return

    # Extract URLs pointing to tar.gz files using regex
    tar_gz_urls = re.findall(r'href=["\'](.*?\.tar\.gz)["\']', response.text)

    if not tar_gz_urls:
        print("No tar.gz URLs found")
        return

    # Download and unzip each tar.gz file
    success = 0
    for url in tqdm(tar_gz_urls):
        download_url = urljoin(html_url, url)
        print(f"Downloading: {download_url}")

        # Download the tar.gz file
        tar_gz_response = requests.get(download_url)
        if tar_gz_response.status_code == 200:
            # Extract the content of the tar.gz file
            with tarfile.open(fileobj=BytesIO(tar_gz_response.content), mode="r:gz") as tar:
                tar.extractall(path="./")  # Extract to the current directory (you can change the path)

            # print(f"Extracted: {url}")
            success += 1
        else:
            print(f"Failed to download: {url}")
    print(f"Extracted {success} files successfully out of {len(tar_gz_urls)} files")
    return f"Extracted {success} files successfully out of {len(tar_gz_urls)} files"

# if __name__ == '__main__':
#     download_and_unzip_from_html(html_page_url)