from twilio.rest import Client
import requests as rq

api_key = "703f09f6854e0881874109f0514a56e1"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC7754033be4d40c8b69e73b89305c376b"
auth_token = "635d686abbd902f6313e3f0d7054a411"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": 29.149240,
    "lon": 75.722580,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = rq.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hourly_data in weather_slice:
    condition_code = (hourly_data["weather"][0]["id"])
    # print(condition_code)
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    print("it will rain")
    message = client.messages.create(
        body="It will rain today, bring an umbrella.",
        from_='+19493045636',
        to='+918607459865'
    )

    print(message.status)
