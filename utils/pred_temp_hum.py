import requests

def get_temp_hum(district, state=None, month=None):
    try:
        # Attempt to read the API key from the file
        with open(".api_key.txt", "r") as file:
            API_KEY = file.read().strip()

        # Use the API key to make a request
        url = f"https://api.openweathermap.org/data/2.5/weather?q={district}&appid={API_KEY}"

        response = requests.get(url)

        # Check for successful API response
        if response.status_code != 200:
            print(response.text)
            raise Exception(f"Unable to get the temperature for {district}")

        # Process the response if successful
        data = response.json()
        humidity = data['main']['humidity']
        temp = (data['main']['temp_min'] + data['main']['temp_max']) / 2 - 273.15  # Convert Kelvin to Celsius
        return (temp, humidity)

    except FileNotFoundError:
        # If the .api_key.txt file is missing, use mock data
        print("API key file '.api_key.txt' not found, using mock data.")
        # Return mock temperature and humidity (e.g., 25°C and 60% humidity)
        return (25.0, 60.0)

    except Exception as e:
        # Handle any other errors (e.g., API request failed)
        print(f"Error: {str(e)}")
        return (25.0, 60.0)  # Fallback to mock data if an error occurs
