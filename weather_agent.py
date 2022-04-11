from bs4 import BeautifulSoup
import requests

# Google: 'what is my user agent' and paste into here
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}


def weather_info(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&hl=en',
        headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    # To find these - use Developer view and check Elements
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(location)
    print(time)
    print(info)
    print(weather+"°C")


weather_info("Copenhagen Weather")
