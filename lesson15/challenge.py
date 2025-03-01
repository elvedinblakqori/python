import requests


def get_weather(city, api_key):
    # Define the base URL for the OpenWeatherMap API
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a request to the API
    response = requests.get(base_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response to JSON format
        weather_data = response.json()

        # Extract data from the JSON response
        main = weather_data['main']
        weather = weather_data['weather'][0]
        wind = weather_data['wind']

        # Print the weather data
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Pressure: {main['pressure']} hPa")

    else:
        # Handle errors (e.g., city not found or wrong API key)
        print("Error: Unable to retrieve weather data. Please check the city name or your API key.")


def main():
    # Prompt the user to enter a city name
    city = input("Enter city name: ")

    # Replace with your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY_HERE'

    # Get the weather information for the city
    get_weather(city, api_key)


if __name__ == "__main__":
    main()
