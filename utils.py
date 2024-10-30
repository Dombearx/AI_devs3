import requests

def get_plain_text_from_url(url: str) -> dict:
    response = requests.get(url)
    return response.text