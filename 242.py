
from math import radians, cos, sin, asin, sqrt

import requests
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def geocode(name: str) :
    params = {
        'q': name,
        'format': 'json',
        'limit': 1,
    }
    headers = {
        'User-Agent': 'MyPythonApp/1.0 (your_email@example.com)'  # Use a descriptive User-Agent
    }
    r = requests.get("https://nominatim.openstreetmap.org/search", params)
    print(f"Status Code: {r.status_code}")
    print(f"Response Content: {r.text}")
    r.raise_for_status()  # will raise an exception for HTTp status code != 200
    data = r.json()

    return (float(data[0]["lat"]), float(data[0]["lon"]))

people = {
    'Udi': '13 Mantur, Modiin, Israel',
    'Donald': 'The White House',
    'Mickey': 'Disneyland',
    'Reuven': 'בית הנשיא',
    'David': 'צריף בן גוריון',
    'Salih': 'עראבה',
    'yousef': 'כפר כנא'
}


def get_closest_and_farthest(people):
    dict={}
    for i in people.keys():
        for j in people.keys():
            if(i,j)or(j,i) not in dict:
                first=geocode(i)
                second=geocode(j)
                dict[(i,j)]=haversine(first[1],first[0],second[1],second[0])
    print(dict)

closest, farthest = get_closest_and_farthest(people)
print(closest, farthest)
assert closest == frozenset(('Udi', 'Reuven'))
assert farthest == frozenset(('David', 'Mickey'))
print("OK")
