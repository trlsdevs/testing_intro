import requests


def save_data_remote(lat, lon):
    res = requests.post('https://my.server.com/cord', json={
        'lat': lat,
        'lon': lon
    })
    return True if res.json() else False
