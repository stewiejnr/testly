import requests
import __main__


def call_restendpoint():
    if __main__.debug == 1:
        print("DEBUG: REST url: ", __main__.host)
    return __main__.sys.exit(0)


class Restly:

    def getStatus(self, URL):
        try:
            HTTPResponse = requests.get(URL)
            print("Status Code for Request: {} ".format(HTTPResponse.status_code))
            return __main__.sys.exit(0)
        except requests.exceptions.RequestException as RaisedException:
            print(RaisedException)
            return __main__.sys.exit(0)
