import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = 'ADD YOUR API KEY HERE'
account_sid = 'ADD YOUR ACCOUNT ID HERE'
auth_token = 'ADD THE AUTHENTICATION TOKEN HERE'

weather_parameters = dict(lat=28.6362211, lon=77.2922332, appid=api_key, exclude='current,minutely,daily')

response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today so, bring your umbrella",
        from_='NUMBER FROM WHICH MESSAGE WILL BE FORWARDED',
        to='NUMBER TO WHICH THE MESSAGE WILL BE FORWARDED'
    )
