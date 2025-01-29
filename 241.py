import requests

from pprint import pprint



import typing

def geocode(name: str) -> typing.Tuple[float, float]:
    params = {
        'q': name,
        'format': 'json',
        'limit': 1,
    }
    headers = {
        'User-Agent': 'MyPythonApp/1.0 (your_email@example.com)'  # Use a descriptive User-Agent
    }
    r = requests.get("https://nominatim.openstreetmap.org/search", params=params, headers=headers)
    r.raise_for_status()  # will raise an exception for HTTp status code != 200
    data = r.json()

    return (float(data[0]["lat"]),float(data[0]["lon"]))


result = geocode('13 Mantur, Modiin, Israel')
pprint(result)  # something like (31.9038434, 35.0156079)
assert abs(result[0] - 31.9038434) < 0.0001
assert abs(result[1] - 35.0156079) < 0.0001

result = geocode('The White House')
print(result)  # something like (38.897699, -77.036553)
assert abs(result[0] - 38.89769) < 0.0001
assert abs(result[1] - -77.03655) < 0.0001
print("OK")