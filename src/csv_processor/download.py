import requests

def download_csv(url: str, local_path: str) -> None:
    """
    Download a CSV file from URL and save locally using streaming for large files.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise error on bad status
    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)