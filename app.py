import requests

def fetch_data(url):
    # Remediación: Se eliminó la credencial hardcodeada
    response = requests.get(url)
    return response.json()