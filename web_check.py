# web_check.py
import requests  # This package is found because venv is active

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Connection successful!")
        else:
            print("Connection failed or redirected.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

check_website('https://www.google.com')
