import os
import requests

def download_and_replace_file(url):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    local_file_path = os.path.join(script_directory, os.path.basename(url))

    response = requests.get(url)

    if response.status_code == 200:
        with open(local_file_path, 'wb') as file:
            file.write(response.content)
        print('File downloaded and replaced successfully.')
    else:
        print('Error downloading file.')

# Example usage:
github_raw_file_url = 'https://raw.githubusercontent.com/FlicksDaModdle/HomeAssetDl/main/Pokemon_Asb_Downloader.py'

download_and_replace_file(github_raw_file_url)
