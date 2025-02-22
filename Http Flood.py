import requests
import threading

target_url = "http://example.com"
num_requests = 1000  # Number of requests to send

def send_request():
    try:
        response = requests.get(target_url)
        print(f"Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

threads = []

for _ in range(num_requests):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
