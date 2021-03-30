import requests
from datetime import datetime

# from fake_headers import Headers


def request_methods():
    # response = requests.get('https://httpbin.org')
    # response = requests.post('https://httpbin.org/post', data={'first_name': 'Pavlo', 'last_name': 'Myha'})
    # response = requests.put('https://httpbin.org/put', data={'key': 'value'})
    # response = requests.delete('https://httpbin.org/delete')
    # response = requests.head('https://httpbin.org/get')
    # response = requests.options('https://httpbin.org/get')
    print('response.status_code============', response.status_code)
    print('response.json============', response.json())
    print('response.headers============', response.headers)


def response_object():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    # response = requests.get(url)
    response = requests.get(url, timeout=0.5)
    # response_headers = response.headers
    # print('response.headers============', response_headers)
    # print('response.headers_Content-Type============', response_headers['Content-Type'])
    print('response.status_code============', response.status_code)
    # print('response.url============', response.url)
    # print('response.encoding============', response.encoding)
    # print('response.content============', response.content)
    # print('response.text============', response.text)
    # print('response.json============', response.json())


def request_with_params():

    current_date = datetime.now()
    print('current_date', current_date)
    str_current_date = current_date.strftime('%d.%m.%Y')

    url = 'https://api.privatbank.ua/p24api/exchange_rates?json'
    params = dict(date=str_current_date)
    print('params', params)
    auth = "jkhsdfjklhdui"
    headers = {'COntent-type': 'application/json'}

    response = requests.get(url, params=params)
    print('response.headers============', response.headers)
    print('response.status_code============', response.status_code)
    print('response.url============', response.url)
    print('response.encoding============', response.encoding)

    response_text = response.text
    print('response.text============', response_text)


# def post_request():
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # payload = [('key1', 'value1'), ('key1', 'value2')]
    # payload = {'key1': ['value1', 'value2']}
    # response = requests.post("https://httpbin.org/post", data=payload)
    # payload= {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
    # response = requests.post("https://httpbin.org/post", files=payload)
    # print('response.text============', response.text)


# def bad_request():
#     response = requests.get('https://httpbin.org/status/404')
#     # response = requests.get('https://httpbin.org/get')
#     print('response.status_code============', response.status_code)
#     print(response.raise_for_status())


# def cookies_request():
#     session = requests.Session()
#     url = 'http://google.com'
#     session.get(url)
#     print('response.cookies============', session.cookies.get_dict())


def privat_fake_headers():
    headers = Headers(os="mac", headers=True).generate()
    print('headers============', headers)
    current_date = datetime.now()
    str_current_date = current_date.strftime('%d.%m.%Y')
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json'
    params = dict(date=str_current_date)
    response = requests.get(url, params=params, headers=headers)
    print('response_headers============', response.headers)


if __name__ == "__main__":
    # request_methods()
    # response_object()
    request_with_params()
    # post_request()
    # bad_request()
    # cookies_request()
    # privat_fake_headers()

    #Exceptions
    # # Timeout
    # try:
    #     response = requests.get('https://httpbin.org/user-agent', timeout=(0.00001, 10))
    # except requests.exceptions.ConnectTimeout:
    #     print('Oops. Connection timeout occured!')

    # try:
    #     response = requests.get('https://httpbin.org/user-agent', timeout=(10, 0.0001))
    # except requests.exceptions.ReadTimeout:
    #     print('Oops. Read timeout occured')
    # except requests.exceptions.ConnectTimeout:
    #     print('Oops. Connection timeout occured!')


    # ConnectionError
    # try:
    #     response = requests.get('http://urldoesnotexistforsure.bom')
    # except requests.exceptions.ConnectionError:
    #     print('Seems like dns lookup failed..')



    # HTTPError
    # try:
    #     response = requests.get('https://httpbin.org/status/500')
    #     response.raise_for_status()
    # except requests.exceptions.HTTPError as err:
    #     print('Oops. HTTP Error occured')
    #     print(f'Response is: {err.response}')
