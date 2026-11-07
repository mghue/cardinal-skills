# Cardinal Skills — a Hermes skill tap

A small, original Hermes skill tap developed for a personal-assistant assignment
with Codex assistance. It contains **cardinal-weather**, a city forecast skill
using a bundled standard-library Python client for Open-Meteo. It needs no paid
API key and preserves explicit location, units, forecast timezone and attribution.

## Install through the Hermes Skills Hub

On an initialized Hermes installation:

```bash
hermes skills tap add mghue/cardinal-skills
hermes skills search cardinal-weather
hermes skills install mghue/cardinal-skills/skills/cardinal-weather
```

Load `cardinal-weather` in Hermes and ask: “What is the weather in Los Angeles,
US? Include the source, temperature units and forecast timezone.” The agent
loads the skill and invokes the bundled script. Installing only a direct
SKILL.md URL is not the supported distribution method.

The assignment submission records the public repository commit and a separate
fresh-install transcript after publication. That evidence has not been created
at preparation time. Use the recorded commit to reproduce the submitted version.

## Run the helper independently

```bash
python3 skills/cardinal-weather/scripts/weather.py 'Los Angeles' --country US
```

Python 3.9+ and HTTPS access to `geocoding-api.open-meteo.com` and
`api.open-meteo.com` are required. No account, environment secret, location
permission, package installer, or background process is used. City resolution
chooses the first result and returns its identity; users must confirm ambiguous
names before relying on the forecast.

## Data and limitations

Data is from [Open-Meteo](https://open-meteo.com/), with
[API documentation](https://open-meteo.com/en/docs) and
[terms/licensing](https://open-meteo.com/en/terms). Attribute the data provider.
This is an educational, noncommercial use. Check the provider's current terms
and limits for other uses. API availability and rate limits can cause failures;
this is not a safety-critical weather alert service.

Source code is MIT licensed. The initial code, documentation and verification
were developed with Codex assistance and are disclosed as such.
