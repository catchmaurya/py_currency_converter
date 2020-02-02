import requests
import logging
import configparser
from datetime import date, datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()

country_codes = ['AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP',
                 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW',
                 'KZT', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR',
                 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'UAH', 'USD', 'UYU', 'ZAR']


class Error(Exception):
   """Base class for other exceptions"""
   pass

class UnsupportedCountryCode(Error):

    def __init__(self,  param='', payload=None):
        self.param = param
        self.payload = payload


class InvalidAmount(Error):

    def __init__(self,  payload=None):
        self.payload = payload

class InvalidDate(Error):

    def __init__(self,  payload=None):
        self.payload = payload


def load_config():
    config.read('./config.ini')
    return config['DEFAULT']['restapi_url']

def consume_api(base ):
    url = load_config()
    response = requests.get(url + base)
    if response.status_code == 200:
        result = response.json()
    else:
        result = {}
    return result



def convert(base='USD', date_text=date.today(), amount=1, to=[]):
    try:
        if base not in country_codes:
            raise UnsupportedCountryCode("base", base)

        if len(to) > 0:
            diff = set(to)-set(country_codes)
            if diff:
                raise UnsupportedCountryCode("to", list(diff))

        if type(amount) not in (int, float):
            raise InvalidAmount(amount)
            if amount < 0:
                raise InvalidAmount(amount)

        # try:
        #     datetime.strptime(date_text, '%Y-%m-%d')
        # except ValueError:
        #     raise InvalidDate(date_text)

        output = consume_api(base)
        if output == {}:
            print("some issues with doing API call")
        else:
            rates = output['rates']

            if to == []: to = country_codes
            output=dict(zip(to,[*map(lambda country_code:amount*rates[country_code], to)]))
            print(output)

        pass
    except UnsupportedCountryCode as error:
        print(error.param + ':: ' + str(error.payload) + " is not supported ")
    except InvalidAmount as error:
        print("amount ::" + str(error.payload) + " is not supported ")
    except InvalidDate as error:
        print("date ::" + str(error.payload) + " is not supported. try YYYY-MM-DD format.")


# convert(base='USD', amount=1, to=['SGD', 'EUR'])
convert(amount=1, to=['SGD', 'EUR'])

