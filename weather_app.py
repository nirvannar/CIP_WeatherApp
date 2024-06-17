import requests
from configparser import ConfigParser

def main():
        
    while True:
        city = input("Enter city name and country code (if required) or 'exit' to quit: ")
        if city.lower() == 'exit':
            print("Exiting the weather app.")
            break
        get_weather(city)   
      
def get_weather(city):
        """
    This function receives the city and returns the weather details of the city or an error. 
    """

        api_key =  get_api_key()
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        try:
                response = requests.get(url)
                data = response.json()
                temp = data['main']['temp']
                feel = data['main']['feels_like']
                high = data['main']['temp_max']
                low = data['main']['temp_min']

                desc = data['weather'][0]['description']
                weather_id = data['weather'][0]['id']

                weather_symbol = display(weather_id)
                                
                print(f'Temperature: {round(temp,1)}° C  Real feel: {round(feel,1)}° C')
                
                print(f'Maximum: {round(high,1)}° C  Minimum: {round(low,1)}° C')
                print(f'Description: {desc.capitalize()} {weather_symbol}')
                print("")
                                
        except Exception as e:
                print('Error fetching weather data! Please try again')
                print("")

                                
  
def get_api_key():
    """Fetches the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


def display(weather_id):
    """Chooses the symbol to print based on weather_id

    Expects an integer value and compares it to a range and returns a symbol in "text" format

    """
    THUNDERSTORM = range(200, 300)
    DRIZZLE = range(300, 400)
    RAIN = range(500, 600)
    SNOW = range(600, 700)
    ATMOSPHERE = range(700, 800)
    CLEAR = range(800, 801)
    CLOUDY = range(801, 900)

    if weather_id in THUNDERSTORM:
            display_params = ("💥")
    elif weather_id in DRIZZLE:
            display_params = ("💧")
    elif weather_id in RAIN:
            display_params = ("💦")
    elif weather_id in SNOW:
            display_params = ("⛄️")
    elif weather_id in ATMOSPHERE:
            display_params = ("🌀")
    elif weather_id in CLEAR:
            display_params = ("🔆")
    elif weather_id in CLOUDY:
            display_params = ("💨")
    else:  
            display_params = ("🌈")
    return display_params

if __name__ == "__main__":
    main()
   
