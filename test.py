import requests

url = "https://api.themoviedb.org/3/movie/550?api_key=a18e8458d49d87ae35d30e3e6f2b46cd&language=en-US"

response = requests.get(url, timeout=10)
print(response.status_code)
print(response.text)