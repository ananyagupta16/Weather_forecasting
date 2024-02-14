import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to retrieve weather information.")

def main():
    api_key = "d9248f30d5068834319f004a1028d513"  
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather(api_key, location)

    # Display weather information
    display_weather(weather_data)

main()
