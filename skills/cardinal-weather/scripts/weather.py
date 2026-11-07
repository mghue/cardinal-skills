#!/usr/bin/env python3
"""Keyless city forecasts for the Cardinal Weather Hermes skill.
Original assignment implementation developed with Codex assistance, Nov 2026.
Reference: https://open-meteo.com/en/docs
"""
import argparse
from datetime import datetime, timezone
import json
from urllib.parse import urlencode
from urllib.request import urlopen

def fetch_json(url, params):
    with urlopen(url + '?' + urlencode(params), timeout=15) as response:
        return json.load(response)

def weather(city, country=None):
    if not 2 <= len(city) <= 120 or (country and (len(country) != 2 or not country.isalpha())):
        raise ValueError('Provide a city and optional two-letter country code')
    params = {'name': city, 'count': 5, 'language': 'en', 'format': 'json'}
    if country:
        params['countryCode'] = country.upper()
    choices = fetch_json('https://geocoding-api.open-meteo.com/v1/search', params).get('results', [])
    if not choices:
        raise ValueError('City not found')
    location = choices[0]
    forecast = fetch_json('https://api.open-meteo.com/v1/forecast', {
        'latitude': location['latitude'], 'longitude': location['longitude'],
        'current': 'temperature_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m',
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_probability_max',
        'forecast_days': 3, 'timezone': 'auto', 'temperature_unit': 'celsius', 'wind_speed_unit': 'kmh'})
    return {'source': 'Open-Meteo', 'source_url': 'https://open-meteo.com/',
            'retrieved_utc': datetime.now(timezone.utc).isoformat(),
            'location': {key: location.get(key) for key in ('name', 'admin1', 'country', 'latitude', 'longitude')},
            'timezone': forecast.get('timezone'), 'current': forecast.get('current'),
            'current_units': forecast.get('current_units'), 'daily': forecast.get('daily'),
            'daily_units': forecast.get('daily_units')}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('city')
    parser.add_argument('--country', help='Optional ISO two-letter country code')
    args = parser.parse_args()
    try:
        print(json.dumps(weather(args.city, args.country)))
    except Exception as error:
        print(json.dumps({'error': type(error).__name__, 'message': 'Weather request failed; do not invent a forecast.'}))
        raise SystemExit(1)
