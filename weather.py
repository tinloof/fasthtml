import asyncio, httpx

coordinates = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0500, -118.2500),
    "Chicago": (41.8333, -87.6167),
    "Houston": (29.7500, -95.3500),
    "Washington": (38.8833, -77.0333)
}

async def weather(client, city):
    lat,lon = coordinates[city]
    point = (await client.get(f"https://api.weather.gov/points/{lat},{lon}")).json()['properties']
    station_url = point['observationStations']
    stations = (await client.get(station_url)).json()
    first_url = stations['features'][0]['id']
    obs = (await client.get(f"{first_url}/observations/latest")).json()['properties']
    def val(x): return round(x['value'], 1) if x['value'] else 'NA'
    return city, dict(temp=val(obs['temperature']),
                      wind=val(obs['windSpeed']),
                      humid=val(obs['relativeHumidity']))

async def all_weather():
    async with httpx.AsyncClient() as client:
        tasks = [weather(client, city) for city in coordinates]
        results = await asyncio.gather(*tasks)
    return dict(results)
